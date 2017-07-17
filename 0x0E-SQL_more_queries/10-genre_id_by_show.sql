-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id, states.name
       FROM tv_shows, tv_shows_genres
       WHERE tv_shows.id = tv_shows_genre.id
       ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
