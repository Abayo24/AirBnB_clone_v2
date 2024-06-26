-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privileges to the user on the specified database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
