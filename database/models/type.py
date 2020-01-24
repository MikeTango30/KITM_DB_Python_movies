from database.database import execute_query

table_name = "types"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                movie_type_id integer PRIMARY KEY,
                                                movie_id integer,
                                                movie_type_name text NOT NULL,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                ON UPDATE CASCADE,
                                                ON DELETE CASCADE
                                                )""".format(table_name)


def create_movie_type(movie_type, movie_id):
    query = "INSERT INTO {} VALUES(?, ?, ?)".format(table_name)
    params = (movie_type.type_id, movie_id, movie_type.type_name)
    movie_type.type_id = execute_query(query, params, None, True)


def read_movie_type(movie_type_id):
    query = "SELECT * FROM {} WHERE movie_type_id = (?)".format(table_name)
    params = (movie_type_id,)
    execute_query(query, params, True)


def update_movie_id(movie_id, movie_type_id):
    query = "UPDATE {} SET movie_id = (?) WHERE movie_type_id = (?)".format(table_name)
    params = (movie_id, movie_type_id)
    execute_query(query, params)


def update_movie_type_title(movie_type_title, movie_type_id):
    query = "UPDATE {} SET movie_type_title = (?) WHERE movie_type_id = (?)".format(table_name)
    params = (movie_type_title, movie_type_id)
    execute_query(query, params)


def delete_movie_type(movie_type_id):
    query = "DELETE FROM {} WHERE movie_type_id = (?)".format(table_name)
    params = (movie_type_id,)
    execute_query(query, params)
