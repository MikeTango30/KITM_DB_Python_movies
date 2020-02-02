from database.database import execute_query

table_name = "movies_directors"


def create_movies_directors_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                movies_directors_id integer PRIMARY KEY,
                                                movie_id integer,
                                                director_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(director_id) REFERENCES directors(director_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE 
                                                )"""


def create_relationship(movie_id, director_id):
    query = f"""INSERT INTO {table_name} (movie_id, director_id) VALUES(?, ?)"""
    params = (movie_id, director_id)
    execute_query(query, params, None, True)
