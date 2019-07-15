-- a script that creates a table called second_table in the current database
-- creates the table named second_table if it doesn't already exist
CREATE TABLE IF NOT EXISTS `second_table` (id INT,
name VARCHAR(256), score INT);
-- a SQL statement that adds multiple records to a table
INSERT INTO `second_table` (id,name,score) VALUES(1,"John",10),(2,"Alex",3),
(3,"Bob",14),(4,"George",8);
