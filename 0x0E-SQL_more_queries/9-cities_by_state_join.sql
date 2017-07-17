--  lists all cities contained in the database
SELECT id, name FROM cities;
SELECT name FROM states WHERE states.id = cities.id;
ORDER BY id ASC;
