-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- SQL query that retrieves city temperature averages
SELECT `state`, MAX(`value`) as `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `state`
ORDER BY `avg_temp` DESC
LIMIT 3;
