-- a script that lists the number of records with the same score in the table second_table
-- SQL statement that lists number of records with the same score
SELECT score, COUNT(*) as 'number'
       FROM `second_table`
       	    GROUP BY `score` DESC;
