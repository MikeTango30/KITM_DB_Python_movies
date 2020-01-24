from database.database import execute_query

table_name = "movies_actors"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                movies_actors_id integer PRIMARY KEY,
                                                movie_id integer,
                                                actor_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(actor_id) REFERENCES actors(actor_id),
                                                ON UPDATE CASCADE,
                                                ON DELETE CASCADE 
                                                )""".format(table_name)
    execute_query(query)