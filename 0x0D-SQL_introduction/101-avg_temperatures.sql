-- Script to convert  database to UTF8
SELECT `city`, AVG(value) AS 'avg_temp' FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
