-- Create user user_0d_1 with password user_0d_1_pwd
-- Grant all privileges to user_0d_1
-- Script will not fail if user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
