# 🍕 Zomato Clone - Complete Food Delivery Platform

A full-featured food delivery and restaurant discovery platform built with Django and Django REST Framework. This project demonstrates expertise in full-stack development, REST APIs, real-time WebSocket communication, and complex database relationships.

![Django](https://img.shields.io/badge/Django-5.2-green)
![DRF](https://img.shields.io/badge/DRF-3.16-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue)
![Python](https://img.shields.io/badge/Python-3.11+-yellow)

## 🌟 Features

### 🔐 Multi-User System
- **Customer**: Browse restaurants, place orders, track delivery, write reviews
- **Restaurant Owner**: Manage menu, update prices, track incoming orders, update status
- **Delivery Personnel**: View assigned orders, update delivery status
- **Admin**: Complete dashboard to manage everything

### 🎨 Beautiful UI
- **Zomato-like Design**: Modern, responsive interface with red theme
- **Customer Pages**: Browse restaurants, search by cuisine, view menus, order tracking
- **Vendor Dashboard**: Professional dashboard for restaurant owners
- **Mobile Responsive**: Works perfectly on all devices

### 🍽️ Restaurant Management
- Full CRUD operations for restaurants
- Menu categories and food items
- Real-time availability updates
- Search and filter by cuisine type
- Geolocation support

### 🛒 Order Management
- Shopping cart functionality
- Place orders with multiple items
- Order history tracking
- Real-time order status updates (WebSocket)
- Mock payment gateway integration

### ⭐ Reviews & Ratings
- 1-5 star rating system
- Customer reviews for restaurants
- Review management

### 🔧 Advanced Features
- **REST API**: Complete RESTful API with Django REST Framework
- **WebSocket Support**: Real-time notifications using Django Channels
- **Token Authentication**: Secure API access
- **Search & Filter**: Advanced filtering with Django Q objects
- **Admin Panel**: Powerful Django admin customization
- **CORS Enabled**: Ready for frontend integration

## 🚀 Live Demo

**Homepage**: Browse restaurants and cuisines  
**Customer Dashboard**: Track your orders  
**Vendor Dashboard**: Manage your restaurant  

## 📸 Screenshots

### Homepage
![Homepage](screenshots/home.png)

### Restaurant List
![Restaurants](screenshots/restaurants.png)

### Vendor Dashboard
![Vendor](screenshots/vendor.png)

## 🛠️ Tech Stack

- **Backend**: Django 6.0, Django REST Framework 3.16
- **Database**: PostgreSQL 14 (Production), SQLite (Development)
- **Real-time**: Django Channels 4.3, Daphne
- **Authentication**: Token-based (DRF)
- **Deployment**: Gunicorn, WhiteNoise
- **Additional**: django-filter, Pillow, django-cors-headers

## 📁 Project Structure

```
zomato-clone/
├── users/              # User authentication & profiles
├── restaurants/        # Restaurant, menu, food items
├── orders/            # Orders, cart, reviews
├── templates/         # HTML templates
│   ├── auth/         # Login/Register pages
│   ├── customer/     # Customer dashboard
│   ├── vendor/       # Vendor dashboard
│   └── restaurants/  # Restaurant pages
├── zomato_clone/      # Main project settings
├── static/            # CSS, JS, images
├── media/             # User uploaded files
├── .env.example       # Environment variables template
├── requirements.txt   # Python dependencies
├── Procfile          # For deployment
├── runtime.txt       # Python version
└── README.md
```

## 🏃 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 14+ (or SQLite for development)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/zomato-clone.git
cd zomato-clone
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Load demo data (optional)**
```bash
python populate_data.py
```

8. **Run development server**
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📡 API Documentation

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login and get token
- `GET/PUT /api/auth/profile/` - View/update profile

### Restaurants
- `GET /api/restaurant/vendors/` - List all restaurants
- `GET /api/restaurant/vendors/?search=Pizza` - Search restaurants
- `GET /api/restaurant/menu-items/` - List menu items
- `POST /api/restaurant/vendors/` - Create restaurant (Vendor only)

### Orders & Cart
- `GET /api/cart/` - View cart
- `POST /api/cart/` - Add item to cart
- `DELETE /api/cart/{id}/` - Remove from cart
- `POST /api/orders/place_order/` - Place order
- `GET /api/orders/` - View order history
- `POST /api/orders/{id}/update_status/` - Update status
- `POST /api/orders/{id}/pay_order/` - Process payment

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Submit review

### WebSocket
- `ws://localhost:8000/ws/orders/{order_id}/` - Real-time order updates

## 🧪 Testing the API

### Login and Get Token
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

### Place an Order
```bash
curl -X POST http://127.0.0.1:8000/api/orders/place_order/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{
    "vendor_id": 1,
    "items": [
      {"food_item_id": 1, "quantity": 2}
    ]
  }'
```

## 🚀 Deployment

### Deploy to Render

1. Push code to GitHub
2. Create new Web Service on [Render.com](https://render.com)
3. Connect your repository
4. Set environment variables
5. Deploy!

**See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions**

### Deploy to Railway

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

## 🔐 Environment Variables

Create a `.env` file with:

```env
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com

DB_ENGINE=django.db.backends.postgresql
DB_NAME=zomato_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## 📊 Database Models

- **User**: Custom user model with roles (Customer/Vendor/Delivery/Admin)
- **Vendor**: Restaurant profile with location and cuisine type
- **MenuCategory**: Menu categories (e.g., "Pizzas", "Burgers")
- **FoodItem**: Individual menu items with pricing
- **Order**: Customer orders with status tracking
- **OrderItem**: Line items within orders
- **Cart**: Shopping cart for customers
- **Review**: Customer reviews and ratings

## 🎯 Key Features Implemented

✅ User authentication with multiple roles  
✅ Restaurant CRUD operations  
✅ Menu management  
✅ Shopping cart system  
✅ Order placement and tracking  
✅ Real-time WebSocket notifications  
✅ Reviews and ratings  
✅ Search and filter functionality  
✅ Admin dashboard  
✅ RESTful API  
✅ Token-based authentication  
✅ Beautiful responsive UI  

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Pradhyumn Yadav**
- Email: pradhyumnsingh91@gmail.com
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- Django & DRF documentation
- Zomato for design inspiration
- Open source community

---

**⭐ If you like this project, please give it a star!**
