from database.database import execute_query

table_name = "movies_directors"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                movies_directors_id integer PRIMARY KEY,
                                                movie_id integer,
                                                director_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(director_id) REFERENCES directors(director_id),
                                                ON UPDATE CASCADE,
                                                ON DELETE CASCADE 
                                                )""".format(table_name)
    execute_query(query)
