from database.database import execute_query

table_name = "genres"


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                genre_id integer PRIMARY KEY,
                                                genre_name text NOT NULL
                                                )""".format(table_name)
    execute_query(query)


def create_genre(genre):
    query = "INSERT INTO {} VALUES(?, ?)".format(table_name)
    params = (genre.genre_id, genre.genre_name)
    genre.genre_id = execute_query(query, params, None, True)


def read_genre(genre_id):
    query = "SELECT * FROM {} WHERE genre_id = (?)".format(table_name)
    params = (genre_id,)
    execute_query(query, params, True)


def update_genre(genre_name, genre_id):
    query = "UPDATE {} SET genre_name = (?) WHERE genre_id = (?)".format(table_name)
    params = (genre_name, genre_id)
    execute_query(query, params)


def delete_genre(genre_id):
    query = "DELETE FROM {} WHERE genre_id = (?)".format(table_name)
    params = (genre_id,)
    execute_query(query, params)
