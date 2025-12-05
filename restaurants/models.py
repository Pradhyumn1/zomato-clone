from django.db import models
from django.conf import settings

class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_profile')
    restaurant_name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=100, help_text="e.g. Italian, Chinese")
    is_open = models.BooleanField(default=True)
    image = models.ImageField(upload_to='vendor_images/', blank=True, null=True)

    def __str__(self):
        return self.restaurant_name

class MenuCategory(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.vendor.restaurant_name}"

class FoodItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='food_items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.name
