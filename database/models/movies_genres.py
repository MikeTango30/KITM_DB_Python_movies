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


def create_relationship(movie_id, genre_id):
    query = f"""INSERT INTO {table_name} (movie_id, genre_id) VALUES(?, ?)"""
    params = (movie_id, genre_id)
    execute_query(query, params, None, True)
