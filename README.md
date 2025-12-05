# 🍕 Zomato Clone - Food Delivery Platform

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Pradhyumn1-black.svg)](https://github.com/Pradhyumn1)

A full-featured food delivery and restaurant management platform built with Django and Django REST Framework. Features include multi-role user system, real-time order tracking, restaurant management, and complete REST API.

🌐 **Live Demo**: [Portfolio Site](https://pradhyumn1.github.io/zomato-clone/)

---

## ✨ Features

### 🔐 **Multi-Role System**
- Customer, Restaurant Owner, Delivery, and Admin roles
- Token-based authentication
- Secure user management

### 🍽️ **Restaurant Management**
- Browse and search restaurants
- Filter by cuisine type
- Real-time availability updates
- Menu categories and food items

### 🛒 **Order System**
- Shopping cart functionality
- Place and track orders
- Real-time order status (WebSocket)
- Order history

### ⭐ **Reviews & Ratings**
- 1-5 star rating system
- Customer reviews
- Restaurant feedback

### 🎨 **Modern UI**
- Zomato-like responsive design
- Customer and vendor dashboards
- Beautiful landing pages

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2, Django REST Framework 3.16
- **Database**: PostgreSQL / SQLite
- **Real-time**: Django Channels, WebSocket
- **Authentication**: Token-based (DRF)
- **Deployment**: Gunicorn, Railway, Render

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Pradhyumn1/zomato-clone.git
cd zomato-clone
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Load Demo Data (Optional)
```bash
python populate_data.py
```

### 7. Run Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register user
- `POST /api/auth/login/` - Get auth token
- `GET /api/auth/profile/` - User profile

### Restaurants
- `GET /api/restaurant/vendors/` - List restaurants
- `GET /api/restaurant/menu-items/` - Menu items
- `POST /api/restaurant/vendors/` - Create restaurant (Vendor)

### Orders
- `GET /api/cart/` - View cart
- `POST /api/cart/` - Add to cart
- `POST /api/orders/place_order/` - Place order
- `GET /api/orders/` - Order history

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Submit review

---

## 🌐 Deployment

### Deploy to Railway (Free)
1. Visit [railway.app](https://railway.app/)
2. Sign in with GitHub
3. Deploy from: `Pradhyumn1/zomato-clone`
4. Add PostgreSQL database
5. Set environment variables
6. Deploy!

### Deploy to Render
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 📁 Project Structure

```
zomato-clone/
├── users/              # User authentication
├── restaurants/        # Restaurant management
├── orders/             # Orders & cart
├── templates/          # HTML templates
├── docs/              # GitHub Pages
├── requirements.txt   # Dependencies
├── Procfile          # Deployment
├── runtime.txt       # Python version
└── README.md
```

---

## 🔑 Environment Variables

Create `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=.railway.app,.onrender.com
DATABASE_URL=your-database-url
```

---

## 🤝 Contributing

Contributions welcome! Please fork and submit a PR.

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

## 👨‍💻 Author

**Pradhyumn Yadav**
- GitHub: [@Pradhyumn1](https://github.com/Pradhyumn1)
- Email: pradhyumnsingh91@gmail.com

---

## 🙏 Acknowledgments

- Django & DRF Documentation
- Zomato for design inspiration
- Open source community

---

⭐ **Star this repo if you find it helpful!**
