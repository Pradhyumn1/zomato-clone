# Heroku Deployment Guide - Zomato Clone

## 🚀 Deploy to Heroku (Easy & Free)

### Prerequisites
- Heroku account (sign up at https://heroku.com)
- Heroku CLI installed

---

## 📦 **Method 1: Deploy via Heroku CLI (Easiest)**

### Step 1: Install Heroku CLI

**For macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**For Windows:**
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login to Heroku

```bash
heroku login
```

This will open your browser for authentication.

### Step 3: Create Heroku App

```bash
cd "/Users/pradhyumnyadav/Desktop/django pro"
heroku create zomato-clone-pradhyumn
```

### Step 4: Add PostgreSQL Database

```bash
heroku addons:create heroku-postgresql:essential-0
```

This automatically sets the `DATABASE_URL` environment variable.

### Step 5: Set Environment Variables

```bash
heroku config:set SECRET_KEY="django-insecure-n15cz4=d627)h%e^30g^@6+uug&1#vkkp(%dj7$53gfn0+*vh"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=".herokuapp.com"
heroku config:set PYTHON_VERSION=3.11.7
```

### Step 6: Deploy!

```bash
git push heroku main
```

### Step 7: Run Migrations

```bash
heroku run python manage.py migrate
```

### Step 8: Create Superuser

```bash
heroku run python manage.py createsuperuser
```

### Step 9: Load Demo Data (Optional)

```bash
heroku run python populate_data.py
```

### Step 10: Open Your App!

```bash
heroku open
```

Your app will be live at: `https://zomato-clone-pradhyumn.herokuapp.com`

---

## 📦 **Method 2: Deploy via Heroku Dashboard (No CLI)**

### Step 1: Create Account
1. Go to https://heroku.com
2. Sign up for free account
3. Verify your email

### Step 2: Create New App
1. Click **"New"** → **"Create new app"**
2. App name: `zomato-clone-pradhyumn` (must be unique)
3. Region: Choose closest to you
4. Click **"Create app"**

### Step 3: Connect GitHub
1. Go to **"Deploy"** tab
2. Click **"Connect to GitHub"**
3. Search for: `Pradhyumn1/zomato-clone`
4. Click **"Connect"**

### Step 4: Add PostgreSQL
1. Go to **"Resources"** tab
2. In "Add-ons" search box, type: `Heroku Postgres`
3. Select **"Heroku Postgres"**
4. Choose plan: **"Essential-0"** (Free)
5. Click **"Submit Order Form"**

### Step 5: Set Environment Variables
1. Go to **"Settings"** tab
2. Click **"Reveal Config Vars"**
3. Add these (DATABASE_URL is already added):

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `django-insecure-n15cz4=d627)h%e^30g^@6+uug&1#vkkp(%dj7$53gfn0+*vh` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.herokuapp.com` |
| `PYTHON_VERSION` | `3.11.7` |

### Step 6: Deploy
1. Go back to **"Deploy"** tab
2. Scroll to **"Manual deploy"**
3. Select branch: `main`
4. Click **"Deploy Branch"**
5. Wait 5-10 minutes

### Step 7: Run Commands
1. Click **"More"** (top right) → **"Run console"**
2. Run these commands one by one:

```bash
python manage.py migrate
python manage.py createsuperuser
python populate_data.py
```

### Step 8: View Your App!
1. Click **"Open app"** button (top right)
2. Your site is LIVE!

---

## 🎯 **Your App URLs**

- **Main Site**: https://zomato-clone-pradhyumn.herokuapp.com
- **Admin**: https://zomato-clone-pradhyumn.herokuapp.com/admin/
- **API**: https://zomato-clone-pradhyumn.herokuapp.com/api/

---

## 🔧 **Useful Heroku Commands**

```bash
# View logs
heroku logs --tail

# Run Django shell
heroku run python manage.py shell

# Run any command
heroku run <command>

# Restart app
heroku restart

# Open app in browser
heroku open

# View app info
heroku info
```

---

## ✅ **Auto-Deploy from GitHub**

Enable automatic deployments:
1. Go to **"Deploy"** tab
2. Scroll to **"Automatic deploys"**
3. Select branch: `main`
4. Click **"Enable Automatic Deploys"**

Now every `git push` automatically deploys!

---

## 💰 **Pricing**

- **Free Tier**: 
  - 550-1000 free dyno hours/month
  - App sleeps after 30 min inactivity
  - PostgreSQL: 10,000 rows limit

- **Hobby Tier** ($7/month):
  - Always-on (no sleeping)
  - 10,000,000 rows PostgreSQL
  - Custom domains

---

## 🐛 **Troubleshooting**

### App Crashed?
```bash
heroku logs --tail
```

### Database Issues?
```bash
heroku pg:info
heroku pg:psql  # Access database directly
```

### Need to Reset Database?
```bash
heroku pg:reset DATABASE_URL
heroku run python manage.py migrate
```

---

## 🎊 **You're Done!**

Your Zomato Clone is now live on Heroku! 🚀

Visit: https://zomato-clone-pradhyumn.herokuapp.com
