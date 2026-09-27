# Last updated: 9/27/2026, 3:15:00 PM
SELECT a.id
FROM Weather a, Weather b
WHERE DATEDIFF(a.recordDate, b.recordDate) = 1
  AND a.temperature > b.temperature;
