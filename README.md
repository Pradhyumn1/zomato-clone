# Zomato Clone - Complete Food Delivery Platform

A full-featured food delivery and restaurant discovery platform built with Django REST Framework. This project demonstrates expertise in full-stack development, REST APIs, real-time WebSocket communication, and complex database relationships.

## ✨ Features

### 🔐 Authentication & User Management
- Token-based authentication (DRF)
- Multi-role system: Customer, Restaurant Owner, Delivery, Admin
- User registration and profile management

### 🍴 Restaurant Management
- Vendor registration and profile setup
- Menu categories and food items (CRUD operations)
- Restaurant search and filtering (cuisine type, availability)
- Geolocation support (latitude/longitude)

### 🛒 Shopping & Ordering
- Shopping cart functionality
- Place orders with multiple items
- Order history tracking
- Real-time order status updates (WebSocket)
- Mock payment gateway integration

### ⭐ Reviews & Ratings
- Customer reviews for restaurants
- 1-5 star rating system
- Review management

### 🔧 Advanced Features
- Django Channels (WebSocket) for real-time notifications
- Search & Filter (Django Q objects, django-filter)
- Admin dashboard
- CORS enabled for frontend integration
- Production-ready deployment configuration

## 🚀 Tech Stack

- **Backend**: Django 6.0, Django REST Framework 3.16
- **Database**: MySQL (Production), SQLite (Development)
- **Real-time**: Django Channels 4.3, Daphne
- **Deployment**: Gunicorn, WhiteNoise, PostgreSQL (production option)
- **Additional**: django-filter, Pillow, django-cors-headers

## 📁 Project Structure

```
zomato_clone/
├── users/              # User authentication & profiles
├── restaurants/        # Restaurant, menu, food items
├── orders/            # Orders, cart, reviews
├── zomato_clone/      # Main project settings
├── media/             # User uploaded files
├── staticfiles/       # Collected static files (production)
├── manage.py
├── requirements.txt
├── .gitignore
├── Procfile          # For Heroku/Render
├── runtime.txt       # Python version
├── build.sh          # Build script for deployment
└── README.md
```

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- MySQL Server (for production) or SQLite (for development)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/zomato-clone.git
cd zomato-clone
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

#### Option A: MySQL (Recommended for Production)

1. Open MySQL Workbench or terminal
2. Run the SQL script:

```sql
CREATE DATABASE zomato_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Update database credentials in `.env` or `settings.py`:

```python
DB_NAME=zomato_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

#### Option B: SQLite (Quick Start)

```python
# In settings.py, comment out MySQL and uncomment SQLite config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 7: Load Demo Data (Optional)

```bash
python populate_data.py
```

This creates 3 demo restaurants (Dominos, KFC, Wow! Momo) with menu items.

### Step 8: Run Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login and get token
- `GET /api/auth/profile/` - View/update profile

### Restaurants
- `GET /api/restaurant/vendors/` - List all restaurants
- `GET /api/restaurant/vendors/?search=Pizza` - Search restaurants
- `GET /api/restaurant/vendors/?cuisine_type=Italian` - Filter by cuisine
- `POST /api/restaurant/vendors/` - Create restaurant (Vendor only)
- `GET /api/restaurant/menu-items/` - List menu items
- `GET /api/restaurant/categories/` - List categories

### Orders & Cart
- `GET /api/cart/` - View cart
- `POST /api/cart/` - Add item to cart
- `DELETE /api/cart/{id}/` - Remove item from cart
- `DELETE /api/cart/clear_cart/` - Clear entire cart
- `POST /api/orders/place_order/` - Place order
- `GET /api/orders/` - View order history
- `POST /api/orders/{id}/update_status/` - Update order status (Vendor/Delivery)
- `POST /api/orders/{id}/pay_order/` - Process payment (Mock)

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Submit review

### WebSocket
- `ws://127.0.0.1:8000/ws/orders/{order_id}/` - Real-time order status updates

## 🔑 Authentication

All protected endpoints require a token in the Authorization header:

```
Authorization: Token YOUR_TOKEN_HERE
```

### Get Token:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "iamking", "password": "password123"}'
```

## 🌐 Deployment

### Deploy to Render (Recommended)

1. Push code to GitHub
2. Create new Web Service on [Render.com](https://render.com)
3. Set environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app.onrender.com`
   - `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
4. Deploy!

**See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.**

### Deploy to Railway

1. Install Railway CLI: `npm install -g @railway/cli`
2. Run: `railway login`
3. Run: `railway init`
4. Run: `railway up`
5. Add environment variables in Railway dashboard

## 🧪 Testing with Postman

1. Import the API endpoints
2. Set `Authorization` header with token
3. Test all CRUD operations

**Example: Place Order**

```json
POST /api/orders/place_order/
{
  "vendor_id": 1,
  "items": [
    {
      "food_item_id": 1,
      "quantity": 2
    },
    {
      "food_item_id": 3,
      "quantity": 1
    }
  ]
}
```

## 📝 Environment Variables

Create a `.env` file (use `.env.example` as template):

```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=zomato_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or support, please contact: pradhyumnsingh91@gmail.com

## 🎯 Future Enhancements

- [ ] Implement actual payment gateway (Stripe/Razorpay)
- [ ] Add Google Maps integration for delivery tracking
- [ ] Email notifications
- [ ] SMS notifications
- [ ] Coupon/promo code system
- [ ] Delivery partner assignment logic
- [ ] Advanced analytics dashboard
- [ ] Mobile app (React Native/Flutter)

---

**Built with ❤️ using Django & DRF**
