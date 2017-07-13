-- lists all records of the table second_table only with name values
SELECT score, name FROM second_table WHERE name is not NULL ORDER BY score DESC;
