# Deployment Guide for Zomato Clone

## Important: Django Deployment Strategy

**Netlify** is designed for static sites and serverless functions. For a Django backend, you have these options:

### Option 1: Recommended Approach (Split Stack)
- **Backend (Django API)**: Deploy to **Render**, **Railway**, or **Heroku**
- **Frontend**: Deploy HTML/React frontend to **Netlify**

### Option 2: All-in-One Platform
- Deploy everything to **Render** or **Railway** (they support Django + static files)

---

## Deploying Django Backend to Render (Free Tier)

### Step 1: Prepare Your Project

1. **Install production dependencies**:
```bash
pip install gunicorn psycopg2-binary python-decouple whitenoise
pip freeze > requirements.txt
```

2. **Create `runtime.txt`**:
```
python-3.11.7
```

3. **Create `build.sh`**:
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Make it executable:
```bash
chmod +x build.sh
```

### Step 2: Update Settings for Production

Add to `settings.py`:
```python
import os
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise to middleware (after SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    ...
]
```

### Step 3: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Zomato Clone"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/zomato-clone.git
git push -u origin main
```

### Step 4: Deploy on Render

1. Go to [render.com](https://render.com) and sign up
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: zomato-clone-api
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn zomato_clone.wsgi:application`
   - **Plan**: Free

5. Add Environment Variables:
   - `DEBUG=False`
   - `SECRET_KEY=your-secret-key-here`
   - `DB_NAME=zomato_db`
   - `DB_USER=your_db_user`
   - `DB_PASSWORD=your_db_password`
   - `DB_HOST=your_render_postgres_host`
   - `DB_PORT=5432`
   - `ALLOWED_HOSTS=your-app-name.onrender.com`

6. Click **Create Web Service**

### Step 5: Set Up PostgreSQL on Render

1. Click **New +** → **PostgreSQL**
2. Name it `zomato-db`
3. Copy the connection details to your web service environment variables

---

## Alternative: Deploy to Railway

1. Visit [railway.app](https://railway.app)
2. Click **Start a New Project**
3. Select **Deploy from GitHub repo**
4. Choose your repository
5. Railway auto-detects Django and configures everything
6. Add environment variables in the **Variables** tab

---

## Frontend Deployment (If you build one)

If you create a React/HTML frontend:

1. Build the frontend:
```bash
npm run build
```

2. Deploy the `build/` folder to Netlify:
   - Drag & drop to Netlify, or
   - Connect GitHub repo
   - Set build command: `npm run build`
   - Set publish directory: `build`

3. Update API URLs in frontend to point to your Render/Railway backend URL

---

## Post-Deployment Checklist

- [ ] Configure CORS to allow frontend domain
- [ ] Set up custom domain (optional)
- [ ] Enable HTTPS (automatic on Render/Netlify)
- [ ] Set DEBUG=False in production
- [ ] Configure email backend for password resets
- [ ] Set up monitoring (Sentry, etc.)
- [ ] Backup database regularly

---

## Current Project Status

✅ MySQL configured (local development)
✅ All models created (User, Vendor, Food, Order, Cart, Review)
✅ All API endpoints implemented
✅ Real-time WebSocket notifications (Channels)
✅ Mock payment integration
✅ Search/Filter functionality
✅ Authentication (Token-based)
✅ Cart system

**Ready for deployment!**
