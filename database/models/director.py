from database.database import execute_query

table_name = "directors"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                director_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )""".format(table_name)


def create_director(director):
    query = "INSERT INTO {} VALUES(?, ?, ?)".format(table_name)
    params = (director.director_id, director.first_name, director.last_name)
    director.director_id = execute_query(query, params, None, True)


def read_director(director_id):
    query = "SELECT * FROM {} WHERE director_id = (?)".format(table_name)
    params = (director_id,)
    execute_query(query, params, True)


def update_name(director_first_name, director_id):
    query = "UPDATE {} SET first_name = (?) WHERE director_id = (?)".format(table_name)
    params = (director_first_name, director_id)
    execute_query(query, params)


def update_last_name(director_last_name, director_id):
    query = "UPDATE {} SET last_name = (?) WHERE director_id = (?)".format(table_name)
    params = (director_last_name, director_id)
    execute_query(query, params)


def delete_director(director_id):
    query = "DELETE FROM {} WHERE director_id = (?)".format(table_name)
    params = (director_id,)
    execute_query(query, params)
