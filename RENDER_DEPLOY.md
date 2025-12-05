# Render Deployment Guide

## Quick Deploy to Render

### Step 1: Push Latest Changes

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (easiest way)
3. Authorize Render to access your GitHub

### Step 3: Create PostgreSQL Database

1. Click **New +** → **PostgreSQL**
2. Name: `zomato-db`
3. Database: `zomato_db`
4. User: `zomato_user`
5. Region: Choose closest to you
6. Plan: **Free**
7. Click **Create Database**
8. **Copy the Internal Database URL** (it starts with `postgresql://`)

### Step 4: Create Web Service

1. Click **New +** → **Web Service**
2. Connect your repository: `Pradhyumn1/zomato-clone`
3. Configure:
   - **Name**: `zomato-clone`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn zomato_clone.wsgi:application`
   - **Plan**: **Free**

### Step 5: Add Environment Variables

Click **Advanced** → **Add Environment Variable**

Add these variables:

```
SECRET_KEY = django-insecure-n15cz4=d627)h%e^30g^@6+uug&1#vkkp(%dj7$53gfn0+*vh
DEBUG = False
ALLOWED_HOSTS = .onrender.com
DATABASE_URL = <paste your Internal Database URL from Step 3>
PYTHON_VERSION = 3.11.7
```

### Step 6: Deploy!

1. Click **Create Web Service**
2. Wait 5-10 minutes for deployment
3. Render will:
   - Install dependencies
   - Run migrations
   - Start the server

### Step 7: Access Your Site

Your site will be live at: `https://zomato-clone.onrender.com`

### Step 8: Create Superuser

1. Go to your Render dashboard
2. Click on your web service
3. Go to **Shell** tab
4. Run:
```bash
python manage.py createsuperuser
```

### Step 9: Load Demo Data (Optional)

In the Render Shell:
```bash
python manage.py shell
```

Then paste:
```python
exec(open('populate_data.py').read())
```

## Troubleshooting

### Database Connection Error
- Make sure DATABASE_URL is correct
- Check that web service and database are in same region

### Static Files Not Loading
- Make sure build.sh is executable
- Check that collectstatic ran successfully

### Server Error 500
- Set DEBUG=True temporarily to see error
- Check logs in Render dashboard

## Important Notes

- **Free tier sleeps after inactivity** - first request may be slow
- **Database limited to 90 days** on free tier
- **Upgrade to paid tier** for production use

## Your Deployed URLs

- **Main Site**: https://zomato-clone.onrender.com
- **Admin Panel**: https://zomato-clone.onrender.com/admin/
- **API**: https://zomato-clone.onrender.com/api/

## Custom Domain (Optional)

1. Buy a domain (e.g., from Namecheap)
2. In Render dashboard → Settings → Custom Domain
3. Add your domain
4. Update DNS records as instructed
