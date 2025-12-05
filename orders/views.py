from rest_framework import viewsets, permissions, status, decorators
from rest_framework.response import Response
from django.db import transaction
from .models import Order, OrderItem, Review, Cart
from .serializers import OrderSerializer, ReviewSerializer, CartSerializer
from restaurants.models import FoodItem, Vendor

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'CUSTOMER':
            return Order.objects.filter(customer=user)
        elif user.role == 'VENDOR':
            return Order.objects.filter(vendor__user=user)
        elif user.role == 'DELIVERY':
            # Simplified: Delivery sees all ready orders or assigned ones
            return Order.objects.filter(status__in=['READY', 'OUT_FOR_DELIVERY'])
        return Order.objects.none()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @decorators.action(detail=False, methods=['post'])
    def place_order(self, request):
        # Expects: { "vendor_id": 1, "items": [{"food_item_id": 1, "quantity": 2}, ...] }
        data = request.data
        vendor_id = data.get('vendor_id')
        items = data.get('items', [])

        if not vendor_id or not items:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            order = Order.objects.create(customer=request.user, vendor=vendor, status='NEW')
            total_amount = 0

            for item in items:
                food_id = item.get('food_item_id')
                qty = item.get('quantity', 1)
                try:
                    food = FoodItem.objects.get(id=food_id)
                    price = food.price
                    OrderItem.objects.create(order=order, food_item=food, quantity=qty, price=price)
                    total_amount += price * qty
                except FoodItem.DoesNotExist:
                    continue # Or raise error
            
            order.total_amount = total_amount
            order.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    @decorators.action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')
        
        # Simple permission check
        if request.user.role == 'VENDOR' and order.vendor.user != request.user:
             return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)
        
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            
            # Send notification
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'order_{order.id}',
                {
                    'type': 'order_status_update',
                    'status': new_status
                }
            )
            
            return Response({"status": "updated"})
        return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

    @decorators.action(detail=True, methods=['post'])
    def pay_order(self, request, pk=None):
        order = self.get_object()
        # Mock payment logic
        # In real life, verify with Stripe/Razorpay
        payment_success = True 
        
        if payment_success:
            order.status = 'PREPARING' # Or 'PAID' if we had that status
            order.save()
            return Response({"status": "Payment successful", "order_status": order.status})
        return Response({"error": "Payment failed"}, status=status.HTTP_400_BAD_REQUEST)

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        # Check if item already in cart, update quantity instead
        food_item = serializer.validated_data['food_item']
        cart_item = Cart.objects.filter(customer=self.request.user, food_item=food_item).first()
        
        if cart_item:
            cart_item.quantity += serializer.validated_data.get('quantity', 1)
            cart_item.save()
            return Response(CartSerializer(cart_item).data)
        else:
            serializer.save(customer=self.request.user)

    @decorators.action(detail=False, methods=['delete'])
    def clear_cart(self, request):
        Cart.objects.filter(customer=request.user).delete()
        return Response({"status": "Cart cleared"}, status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
