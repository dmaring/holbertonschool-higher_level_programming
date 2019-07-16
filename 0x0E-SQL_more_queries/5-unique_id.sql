-- a script that creates the table unique_id
-- creates the table unique_id with id and name attributes
CREATE TABLE IF NOT EXISTS `unique_id` (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
