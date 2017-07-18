-- displays the average temperature by city
SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE temperatures.month in (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
