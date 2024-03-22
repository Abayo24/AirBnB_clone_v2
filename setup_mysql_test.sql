-- Create database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user if it doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privileges to user on specified db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
