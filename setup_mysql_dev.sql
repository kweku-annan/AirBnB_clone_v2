-- Preparing a MySQL server for the project

-- Creating databass
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;

-- Creating a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting privileges to user
GRANT ALL PRIVILEGES ON *.* TO
'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Granting select privilege to user
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost'
FLUSH PRIVILEGES;
