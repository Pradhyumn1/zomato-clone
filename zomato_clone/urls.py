from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (home, restaurant_list, restaurant_detail, 
                   customer_dashboard, vendor_dashboard,
                   login_view, register_view, logout_view)

urlpatterns = [
    path('', home, name='home'),
    path('restaurants/', restaurant_list, name='restaurant_list'),
    path('restaurant/<int:vendor_id>/', restaurant_detail, name='restaurant_detail'),
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
    path('vendor/dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/restaurant/', include('restaurants.urls')),
    path('api/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
