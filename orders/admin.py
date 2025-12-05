from django.contrib import admin
from .models import Order, OrderItem, Review, Cart

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['food_item', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'vendor', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'created_at', 'vendor']
    search_fields = ['customer__username', 'vendor__restaurant_name']
    readonly_fields = ['customer', 'vendor', 'total_amount', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    
    def has_add_permission(self, request):
        return False

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'food_item', 'quantity', 'price']
    list_filter = ['order__vendor']
    search_fields = ['food_item__name']
    
    def has_add_permission(self, request):
        return False

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer', 'food_item', 'quantity', 'total_price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['customer__username', 'food_item__name']
    readonly_fields = ['created_at', 'total_price']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['customer', 'vendor', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'vendor']
    search_fields = ['customer__username', 'vendor__restaurant_name', 'comment']
    readonly_fields = ['created_at']
