-- script that creates a table and a user and sets select privileges for the user
-- SQL statement creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- SQL statement creates a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- SQL statement sets privileges for the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
