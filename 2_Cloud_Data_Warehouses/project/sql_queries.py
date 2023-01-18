import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

DWH_ROLE_ARN = config.get("IAM","ROLE_ARN")
LOG_DATA = config.get("S3","LOG_DATA")
LOG_JSONPATH = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")

# DROP TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
staging_events_table_create= ("""
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
    userId INTEGER);
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs INTEGER,
    artist_id VARCHAR,
    artist_latitude FLOAT,
    artist_longitude FLOAT,
    artist_location TEXT,
    artist_name VARCHAR,
    song_id VARCHAR,
    title VARCHAR,
    duration FLOAT,
    year INTEGER);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INTEGER IDENTITY(0,1) NOT NULL PRIMARY KEY,
    start_time TIMESTAMP,
    user_id INTEGER,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INTEGER,
    location TEXT,
    user_agent TEXT);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1),
    level VARCHAR);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR NOT NULL PRIMARY KEY,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR NOT NULL PRIMARY KEY,
    name VARCHAR,
    location TEXT ,
    latitude FLOAT ,
    longitude FLOAT);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP NOT NULL PRIMARY KEY,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday VARCHAR);
""")

# STAGING TABLES
staging_events_copy = ("""
    copy staging_events 
    from {} 
    credentials 'aws_iam_role={}' 
    format as json {} 
    compupdate off 
    region 'us-west-2';
""").format(LOG_DATA, DWH_ROLE_ARN, LOG_JSONPATH)

staging_songs_copy = ("""
    copy staging_songs 
    from {} 
    credentials 'aws_iam_role={}' 
    format as json 'auto' 
    compupdate off 
    region 'us-west-2';
""").format(SONG_DATA, DWH_ROLE_ARN)

# FINAL TABLES
songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time, 
        user_id, 
        level,
        song_id, 
        artist_id, 
        session_id, 
        location, 
        user_agent
    ) 
    SELECT 
        timestamp 'epoch' + se.ts/1000 * interval '1 second', 
        se.userId, 
        se.level, 
        ss.song_id, 
        ss.artist_id, 
        se.sessionId, 
        se.location, 
        se.userAgent
    FROM staging_events se 
    JOIN staging_songs ss ON (se.song = ss.title AND se.artist = ss.artist_name)
    WHERE se.page = 'NextSong';
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id, 
        first_name, 
        last_name, 
        gender, 
        level
    ) 
    SELECT 
        DISTINCT userId, 
        firstName, 
        lastName, 
        gender, 
        level
    FROM staging_events
    WHERE page = 'NextSong' AND userId IS NOT NULL
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id, 
        title, 
        artist_id, 
        year, 
        duration
    )
    SELECT 
        DISTINCT song_id, 
        title, 
        artist_id, 
        year, 
        duration
    FROM staging_songs
    WHERE song_id IS NOT NULL
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id, 
        name, 
        location, 
        latitude, 
        longitude
    )
    SELECT 
        DISTINCT artist_id, 
        artist_name, 
        artist_location, 
        artist_latitude, 
        artist_longitude
    FROM staging_songs
    WHERE artist_id IS NOT NULL
""")

time_table_insert = ("""
    INSERT INTO time (
        start_time, 
        hour, 
        day, 
        week, 
        month, 
        year, 
        weekday
    )
    SELECT 
        DISTINCT start_time, 
        EXTRACT(hour from start_time), 
        EXTRACT(day from start_time), 
        EXTRACT(week from start_time), 
        EXTRACT(month from start_time), 
        EXTRACT(year from start_time), 
        EXTRACT(weekday from start_time)
    FROM songplays
""")

# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
