from rest_framework import serializers
from .models import Order, OrderItem, Review, Cart
from restaurants.serializers import FoodItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    food_item_details = FoodItemSerializer(source='food_item', read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'food_item', 'food_item_details', 'quantity', 'price')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    vendor_name = serializers.CharField(source='vendor.restaurant_name', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'total_amount', 'created_at', 'updated_at')

class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('customer',)

class CartSerializer(serializers.ModelSerializer):
    food_item_details = FoodItemSerializer(source='food_item', read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'food_item', 'food_item_details', 'quantity', 'total_price', 'created_at')
        read_only_fields = ('customer',)
