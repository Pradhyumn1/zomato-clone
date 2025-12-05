from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, MenuCategoryViewSet, FoodItemViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'categories', MenuCategoryViewSet)
router.register(r'menu-items', FoodItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
