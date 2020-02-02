from database.database import execute_query

table_name = "movies_writers"


def create_movies_writers_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                movies_writers_id integer PRIMARY KEY,
                                                movie_id integer,
                                                writer_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(writer_id) REFERENCES writers(writer_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE 
                                                )"""
    execute_query(query)


def create_relationship(movie_id, writer_id):
    query = f"""INSERT INTO {table_name} (movie_id, writer_id) VALUES(?, ?)"""
    params = (movie_id, writer_id)
    execute_query(query, params, None, True)
