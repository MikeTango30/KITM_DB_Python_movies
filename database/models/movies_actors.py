from database.database import execute_query

table_name = "movies_actors"


def create_movies_actors_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                movies_actors_id integer PRIMARY KEY,
                                                movie_id integer,
                                                actor_id integer,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                FOREIGN KEY(actor_id) REFERENCES actors(actor_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE 
                                                )"""
    execute_query(query)


def create_relationship(movie_id, actor_id):
    query = f"""INSERT INTO {table_name} (movie_id, actor_id) VALUES(?, ?)"""
    params = (movie_id, actor_id)
    execute_query(query, params, None, True)

