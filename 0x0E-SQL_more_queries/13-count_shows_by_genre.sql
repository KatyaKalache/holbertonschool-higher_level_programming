-- lists all genres and displays the number of shows linked to each
SELECT tv_genres.name,
COUNT(*)
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_genres.name;
