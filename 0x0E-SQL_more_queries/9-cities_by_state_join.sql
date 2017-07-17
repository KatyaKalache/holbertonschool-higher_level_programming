--  lists all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities, states
       WHERE cities.id=states.id ORDER BY id ASC;
