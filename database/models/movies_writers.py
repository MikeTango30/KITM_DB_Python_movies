from database.database import execute_query

table_name = "movies_writers"


def create_movies_writers_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                movies_writers_id integer PRIMARY KEY,
                                                movie_id integer,
                                                writer_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(writer_id) REFERENCES writers(writer_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE 
                                                )""".format(table_name)
    execute_query(query)
