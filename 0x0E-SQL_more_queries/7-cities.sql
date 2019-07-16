-- a script that creates the database hbtn_0d_usa and the table states
-- SQL statement that creates hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- SQL statement that creates the table states
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (id INT NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
)
ENGINE=INNODB;
