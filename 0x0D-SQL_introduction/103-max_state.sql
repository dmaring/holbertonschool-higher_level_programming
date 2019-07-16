-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- SQL query that retrieves city temperature averages
SELECT `state`, MAX(`value`) as `max_temp`
FROM `temperatures`
GROUP BY `state` ASC;
