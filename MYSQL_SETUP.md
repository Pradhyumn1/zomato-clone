# Installation Guide for MySQL

Follow these steps to set up MySQL for the Zomato Clone project:

## 1. Install MySQL Client (if not already installed)

### For macOS:
```bash
brew install mysql
pip install mysqlclient
```

If you get compilation errors, try:
```bash
brew install mysql-client pkg-config
export PKG_CONFIG_PATH="/opt/homebrew/opt/mysql-client/lib/pkgconfig"
pip install mysqlclient
```

## 2. Create Database in MySQL Workbench

1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Run this SQL command:

```sql
CREATE DATABASE zomato_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. Create a user (optional, or use root):

```sql
CREATE USER 'zomato_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON zomato_db.* TO 'zomato_user'@'localhost';
FLUSH PRIVILEGES;
```

## 3. Configure Django

Update your `.env` file (or directly in settings.py):

```
DB_NAME=zomato_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

## 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Create Superuser

```bash
python manage.py createsuperuser
```

## 6. Start Server

```bash
python manage.py runserver
```

## Troubleshooting

If you get "Access denied" errors:
- Check your MySQL password
- Ensure MySQL service is running
- Verify user permissions

If migrations fail:
- Drop and recreate the database
- Check that all app models are properly configured
