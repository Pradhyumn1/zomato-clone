from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vendor, MenuCategory, FoodItem
from .serializers import VendorSerializer, MenuCategorySerializer, FoodItemSerializer

class IsVendorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'VENDOR'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the owner can edit
        return obj.user == request.user

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsVendorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['cuisine_type', 'is_open']
    search_fields = ['restaurant_name', 'cuisine_type']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsVendorOrReadOnly]

    def get_queryset(self):
        # If vendor, show their categories. If customer, show all (or filter by vendor in URL)
        user = self.request.user
        if hasattr(user, 'vendor_profile'):
            return MenuCategory.objects.filter(vendor=user.vendor_profile)
        return MenuCategory.objects.all()

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsVendorOrReadOnly]

    def get_queryset(self):
        # Similar logic
        user = self.request.user
        if hasattr(user, 'vendor_profile'):
            return FoodItem.objects.filter(category__vendor=user.vendor_profile)
        return FoodItem.objects.all()
