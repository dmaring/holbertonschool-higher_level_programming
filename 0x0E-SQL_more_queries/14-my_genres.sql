-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- SQL query that lists all genres of the show Dexter
SELECT tv_genres.name
FROM `tv_show_genres` JOIN `tv_genres`
ON tv_show_genres.genre_id = tv_genres.id
WHERE `show_id` =
      (SELECT `id`
      FROM `tv_shows`
      WHERE `title` = 'Dexter')
ORDER BY name ASC;
