-- lists all the cities of California that can be found in hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id in (SELECT id FROM states WHERE id = 1) ORDER BY cities.id DESC;
