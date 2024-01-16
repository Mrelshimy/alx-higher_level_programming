-- Script to list the number of records with the same score in the table second_table
SELECT score, COUNT(*) FROM `second_table` AS 'number' 
GROUP BY score
ORDER BY number DESC;
