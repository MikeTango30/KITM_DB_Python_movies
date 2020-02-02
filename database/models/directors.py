from database.database import execute_query

table_name = "directors"


def create_directors_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                director_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )"""
    execute_query(query)


def create_director(director):
    query = f"INSERT INTO {table_name} VALUES(?, ?, ?)"
    params = (director.director_id, director.first_name, director.last_name)
    director.director_id = execute_query(query, params, None, True)


def read_director(director_id):
    query = f"SELECT * FROM {table_name} WHERE director_id = (?)"
    params = (director_id,)
    execute_query(query, params, True)


def update_name(director_first_name, director_id):
    query = f"UPDATE {table_name} SET first_name = (?) WHERE director_id = (?)"
    params = (director_first_name, director_id)
    execute_query(query, params)


def update_last_name(director_last_name, director_id):
    query = f"UPDATE {table_name} SET last_name = (?) WHERE director_id = (?)"
    params = (director_last_name, director_id)
    execute_query(query, params)


def delete_director(director_id):
    query = f"DELETE FROM {table_name} WHERE director_id = (?)"
    params = (director_id,)
    execute_query(query, params)
