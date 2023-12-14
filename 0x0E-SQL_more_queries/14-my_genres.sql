-- Select the genre names for the show Dexter Filter to show only Dexter Order the results by genre name in ascending order
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
