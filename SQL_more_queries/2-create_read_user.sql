-- Create database hbtn_0d_2 if it doesn't exist
-- Create user user_0d_2 with password user_0d_2_pwd
-- Grant only SELECT privilege on hbtn_0d_2 database to user_0d_2
-- Script will not fail if database or user already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
