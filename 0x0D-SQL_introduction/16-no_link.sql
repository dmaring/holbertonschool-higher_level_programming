-- script that lists all records of the table second_table
-- SQL statement that returns all records of second_table with filters
SELECT `score`, `name`
       FROM `second_table`
       	    WHERE `name` IS NOT NULL
	    	  ORDER BY `score` DESC;
