from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from restaurants.models import Vendor, FoodItem, MenuCategory
from orders.models import Order, Cart
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def restaurant_list(request):
    vendors = Vendor.objects.filter(is_open=True)
    search = request.GET.get('search', '')
    cuisine = request.GET.get('cuisine', '')
    
    if search:
        vendors = vendors.filter(restaurant_name__icontains=search)
    if cuisine:
        vendors = vendors.filter(cuisine_type__icontains=cuisine)
    
    return render(request, 'restaurants/list.html', {'vendors': vendors})

def restaurant_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    categories = MenuCategory.objects.filter(vendor=vendor).prefetch_related('food_items')
    return render(request, 'restaurants/detail.html', {
        'vendor': vendor,
        'categories': categories
    })

@login_required
def customer_dashboard(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    cart_items = Cart.objects.filter(customer=request.user)
    return render(request, 'customer/dashboard.html', {
        'orders': orders,
        'cart_items': cart_items
    })

@login_required
def vendor_dashboard(request):
    if request.user.role != 'VENDOR':
        messages.error(request, 'Access denied. Vendor account required.')
        return redirect('home')
    
    vendor = get_object_or_404(Vendor, user=request.user)
    orders = Order.objects.filter(vendor=vendor).order_by('-created_at')
    categories = MenuCategory.objects.filter(vendor=vendor)
    
    return render(request, 'vendor/dashboard.html', {
        'vendor': vendor,
        'orders': orders,
        'categories': categories
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'VENDOR':
                return redirect('vendor_dashboard')
            return redirect('customer_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'auth/login.html')

def register_view(request):
    if request.method == 'POST':
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'CUSTOMER')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, role=role)
            login(request, user)
            if role == 'VENDOR':
                return redirect('vendor_dashboard')
            return redirect('customer_dashboard')
    
    return render(request, 'auth/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')
