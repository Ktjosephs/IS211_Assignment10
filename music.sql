DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;

CREATE TABLE Artists (
	artist_id INTEGER PRIMARY KEY,
	artist_name TEXT
);

CREATE TABLE Albums (
	album_id INTEGER PRIMARY KEY,
    album_name TEXT,
    artist_ID INTEGER
);

CREATE TABLE Songs (
	song_id INTEGER PRIMARY KEY,
    Song_name TEXT,
    album_ID INTEGER,
    track_Number INTEGER,
    length INTEGER
);
