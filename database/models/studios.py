from database.database import execute_query

table_name = "studios"


def create_studios_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                studio_id integer PRIMARY KEY,
                                                movie_id integer,
                                                title text NOT NULL,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE
                                                )"""
    execute_query(query)


def create_studio(studio, movie_id):
    query = f"INSERT INTO {table_name} VALUES(?, ?, ?)"
    params = (studio.studio_id, movie_id, studio.studio_title)
    studio.studio_id = execute_query(query, params, None, True)


def read_studio(studio_id):
    query = f"SELECT * FROM {table_name} WHERE studio_id = (?)"
    params = (studio_id,)
    execute_query(query, params, True)


def update_movie_id(movie_id, studio_id):
    query = f"UPDATE {table_name} SET movie_id = (?) WHERE studio_id = (?)"
    params = (movie_id, studio_id)
    execute_query(query, params)


def update_title(studio_title, studio_id):
    query = f"UPDATE {table_name} SET studio_title = (?) WHERE studio_id = (?)"
    params = (studio_title, studio_id)
    execute_query(query, params)


def delete_studio(studio_id):
    query = f"DELETE FROM {table_name} WHERE studio_id = (?)"
    params = (studio_id,)
    execute_query(query, params)
