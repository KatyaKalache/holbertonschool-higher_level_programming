-- lists all the cities of California that can be found in hbtn_0d_usa
SELECT id, name from cities WHERE state_id in(SELECT id from states WHERE name=California );
