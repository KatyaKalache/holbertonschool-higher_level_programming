-- lists all genres and displays the number of shows linked to each
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_genres.id
ORDER BY number_shows DESC;
