-- Zomato Clone Database Setup

-- Create database
CREATE DATABASE IF NOT EXISTS zomato_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (optional - you can use root)
-- CREATE USER 'zomato_user'@'localhost' IDENTIFIED BY 'your_password';
-- GRANT ALL PRIVILEGES ON zomato_db.* TO 'zomato_user'@'localhost';
-- FLUSH PRIVILEGES;

-- Select database
USE zomato_db;

-- Verify database is selected
SELECT DATABASE();
