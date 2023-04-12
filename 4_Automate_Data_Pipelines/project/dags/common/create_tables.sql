DROP TABLE IF EXISTS staging_events;
DROP TABLE IF EXISTS staging_songs;
DROP TABLE IF EXISTS songplays;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS time;

CREATE TABLE IF NOT EXISTS staging_events (
    artist VARCHAR,
    auth VARCHAR,
    firstName VARCHAR,
    gender CHAR(1),
    itemInSession INTEGER,
    lastName VARCHAR,
    length FLOAT,
    level VARCHAR,
    location TEXT,
    method VARCHAR,
    page VARCHAR,
    registration FLOAT,
    sessionId INTEGER,
    song VARCHAR,
    status INTEGER,
    ts BIGINT,
    userAgent TEXT,
    userId INTEGER
);

CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs INTEGER,
    artist_id VARCHAR,
    artist_name VARCHAR,
    artist_latitude FLOAT,
    artist_longitude FLOAT,
    artist_location TEXT,
    song_id VARCHAR,
    title VARCHAR,
    duration FLOAT,
    year INTEGER
);

CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INTEGER IDENTITY(0,1) NOT NULL PRIMARY KEY,
    start_time TIMESTAMP,
    user_id INTEGER,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INTEGER,
    location TEXT,
    user_agent TEXT
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1),
    level VARCHAR
);

CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR NOT NULL PRIMARY KEY,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT
);

CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR NOT NULL PRIMARY KEY,
    name VARCHAR,
    location TEXT ,
    latitude FLOAT ,
    longitude FLOAT
);

CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP NOT NULL PRIMARY KEY,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday VARCHAR
);