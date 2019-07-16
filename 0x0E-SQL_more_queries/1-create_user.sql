-- a script that creates the MySQL server user user_0d_1
-- creates the user and sets password
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- sets the grant for the user to all for all access
GRANT ALL ON *.* TO user_0d_1@localhost;
