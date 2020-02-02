from database.database import execute_query

table_name = "genres"


def create_genres_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                genre_id integer PRIMARY KEY,
                                                genre_name text NOT NULL
                                                )"""
    execute_query(query)


def create_genre(genre):
    query = f"INSERT INTO {table_name} VALUES(?, ?)"
    params = (genre.genre_id, genre.genre_name)
    genre.genre_id = execute_query(query, params, None, True)


def read_genre(genre_id):
    query = f"SELECT * FROM {table_name} WHERE genre_id = (?)"
    params = (genre_id,)
    execute_query(query, params, True)


def update_genre(genre_name, genre_id):
    query = f"UPDATE {table_name} SET genre_name = (?) WHERE genre_id = (?)"
    params = (genre_name, genre_id)
    execute_query(query, params)


def delete_genre(genre_id):
    query = f"DELETE FROM {table_name} WHERE genre_id = (?)"
    params = (genre_id,)
    execute_query(query, params)
