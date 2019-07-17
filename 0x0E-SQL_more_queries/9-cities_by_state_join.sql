-- a script that lists all the cities that can be found in the database hbtn_0d_usa
-- SQL query that lists all cities of California found in hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM `cities` INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
