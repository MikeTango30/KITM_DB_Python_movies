from database.database import execute_query

table_name = "studios"


def create_studios_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                studio_id integer PRIMARY KEY,
                                                movie_id integer,
                                                title text NOT NULL,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE
                                                )""".format(table_name)
    execute_query(query)


def create_studio(studio, movie_id):
    query = "INSERT INTO {} VALUES(?, ?, ?)".format(table_name)
    params = (studio.studio_id, movie_id, studio.title)
    studio.studio_id = execute_query(query, params, None, True)


def read_studio(studio_id):
    query = "SELECT * FROM {} WHERE studio_id = (?)".format(table_name)
    params = (studio_id,)
    execute_query(query, params, True)


def update_movie_id(movie_id, studio_id):
    query = "UPDATE {} SET movie_id = (?) WHERE studio_id = (?)".format(table_name)
    params = (movie_id, studio_id)
    execute_query(query, params)


def update_title(studio_title, studio_id):
    query = "UPDATE {} SET studio_title = (?) WHERE studio_id = (?)".format(table_name)
    params = (studio_title, studio_id)
    execute_query(query, params)


def delete_studio(studio_id):
    query = "DELETE FROM {} WHERE studio_id = (?)".format(table_name)
    params = (studio_id,)
    execute_query(query, params)
