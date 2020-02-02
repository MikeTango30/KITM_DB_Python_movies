from database.database import execute_query

table_name = "writers"


def create_writers_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                writer_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )"""
    execute_query(query)


def create_writer(writer, writer_id=None):
    query = f"INSERT INTO {table_name} VALUES(?, ?, ?)"
    params = (writer.writer_id, writer.first_name, writer.last_name)
    writer.writer_id = execute_query(query, params, None, True)


def read_writer(writer_id):
    query = f"SELECT * FROM {table_name} WHERE writer_id = (?)"
    params = (writer_id,)
    execute_query(query, params, True)


def update_name(writer_first_name, writer_id):
    query = f"UPDATE {table_name} SET first_name = (?) WHERE writer_id = (?)"
    params = (writer_first_name, writer_id)
    execute_query(query, params)


def update_last_name(writer_last_name, writer_id):
    query = f"UPDATE {table_name} SET last_name = (?) WHERE writer_id = (?)"
    params = (writer_last_name, writer_id)
    execute_query(query, params)


def delete_writer(writer_id):
    query = f"DELETE FROM {table_name} WHERE writer_id = (?)"
    params = (writer_id,)
    execute_query(query, params)
