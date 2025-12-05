from rest_framework import serializers
from .models import Vendor, MenuCategory, FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    category_details = serializers.SerializerMethodField()
    
    class Meta:
        model = FoodItem
        fields = '__all__'
    
    def get_category_details(self, obj):
        return {
            'id': obj.category.id,
            'name': obj.category.name,
            'vendor': obj.category.vendor.id
        }

class MenuCategorySerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    categories = MenuCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('user',)
