from django.contrib import admin
from .models import Vendor, MenuCategory, FoodItem

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'user', 'cuisine_type', 'is_open', 'address']
    list_filter = ['is_open', 'cuisine_type']
    search_fields = ['restaurant_name', 'address', 'cuisine_type']
    readonly_fields = ['user']

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor']
    list_filter = ['vendor']
    search_fields = ['name', 'vendor__restaurant_name']

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available']
    list_filter = ['is_available', 'category__vendor']
    search_fields = ['name', 'description']
    list_editable = ['price', 'is_available']
