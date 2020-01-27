from database.database import execute_query

table_name = "movies_genres"


def create_movies_genres_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                movies_genres_id integer PRIMARY KEY,
                                                movie_id integer,
                                                genre_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(genre_id) REFERENCES genres(genre_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE 
                                                )""".format(table_name)
    execute_query(query)
