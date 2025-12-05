import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zomato_clone.settings')
django.setup()

from django.contrib.auth import get_user_model
from restaurants.models import Vendor, MenuCategory, FoodItem
from django.core.files.base import ContentFile

User = get_user_model()

def create_dummy_data():
    print("Creating dummy data...")

    # Create Vendors
    vendors_data = [
        {
            "username": "dominos_owner",
            "email": "dominos@example.com",
            "restaurant_name": "Dominos Pizza",
            "cuisine": "Italian, Pizza",
            "address": "123 Pizza Street, Food City",
            "categories": {
                "Pizzas": [
                    {"name": "Margherita", "price": 12.99, "desc": "Classic cheese pizza"},
                    {"name": "Pepperoni", "price": 15.99, "desc": "Spicy pepperoni"},
                    {"name": "Farmhouse", "price": 14.99, "desc": "Loaded with veggies"}
                ],
                "Sides": [
                    {"name": "Garlic Bread", "price": 4.99, "desc": "Buttery garlic goodness"},
                    {"name": "Choco Lava Cake", "price": 5.99, "desc": "Molten chocolate cake"}
                ]
            }
        },
        {
            "username": "kfc_owner",
            "email": "kfc@example.com",
            "restaurant_name": "KFC",
            "cuisine": "American, Fast Food",
            "address": "456 Fried Chicken Ave, Food City",
            "categories": {
                "Burgers": [
                    {"name": "Zinger Burger", "price": 6.99, "desc": "Crispy chicken fillet"},
                    {"name": "Veg Zinger", "price": 5.99, "desc": "Spicy veg patty"}
                ],
                "Buckets": [
                    {"name": "Hot & Crispy Bucket", "price": 19.99, "desc": "8pc Hot & Crispy chicken"},
                    {"name": "Smoky Grilled Bucket", "price": 21.99, "desc": "8pc Smoky Grilled chicken"}
                ]
            }
        },
        {
            "username": "wow_momo_owner",
            "email": "wowmomo@example.com",
            "restaurant_name": "Wow! Momo",
            "cuisine": "Asian, Momos",
            "address": "789 Dumpling Lane, Food City",
            "categories": {
                "Steamed Momos": [
                    {"name": "Veg Steamed Momo", "price": 3.99, "desc": "Simple and tasty"},
                    {"name": "Chicken Steamed Momo", "price": 4.99, "desc": "Juicy chicken filling"}
                ],
                "Fried Momos": [
                    {"name": "Veg Fried Momo", "price": 4.49, "desc": "Crispy fried momos"},
                    {"name": "Chicken Fried Momo", "price": 5.49, "desc": "Crispy chicken goodness"}
                ]
            }
        }
    ]

    for data in vendors_data:
        # Create User
        user, created = User.objects.get_or_create(
            username=data['username'],
            defaults={
                'email': data['email'],
                'role': 'VENDOR'
            }
        )
        if created:
            user.set_password('password123')
            user.save()
            print(f"Created user: {data['username']}")
        
        # Create Vendor Profile
        vendor, created = Vendor.objects.get_or_create(
            user=user,
            defaults={
                'restaurant_name': data['restaurant_name'],
                'cuisine_type': data['cuisine'],
                'address': data['address'],
                'is_open': True
            }
        )
        if created:
            print(f"Created restaurant: {data['restaurant_name']}")

        # Create Categories and Items
        for cat_name, items in data['categories'].items():
            category, _ = MenuCategory.objects.get_or_create(
                vendor=vendor,
                name=cat_name
            )
            
            for item in items:
                FoodItem.objects.get_or_create(
                    category=category,
                    name=item['name'],
                    defaults={
                        'price': item['price'],
                        'description': item['desc'],
                        'is_available': True
                    }
                )
    
    print("Dummy data creation complete!")

if __name__ == "__main__":
    create_dummy_data()
