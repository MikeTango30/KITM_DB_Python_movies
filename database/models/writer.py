from database.database import execute_query

table_name = "writers"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                writer_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )""".format(table_name)
    execute_query(query)


def create_writer(writer, writer_id=None):
    query = "INSERT INTO {} VALUES(?, ?, ?)".format(table_name)
    params = (writer.writer_id, writer.first_name, writer.last_name)
    writer.writer_id = execute_query(query, params, None, True)


def read_writer(writer_id):
    query = "SELECT * FROM {} WHERE writer_id = (?)".format(table_name)
    params = (writer_id,)
    execute_query(query, params, True)


def update_name(writer_first_name, writer_id):
    query = "UPDATE {} SET first_name = (?) WHERE writer_id = (?)".format(table_name)
    params = (writer_first_name, writer_id)
    execute_query(query, params)


def update_last_name(writer_last_name, writer_id):
    query = "UPDATE {} SET last_name = (?) WHERE writer_id = (?)".format(table_name)
    params = (writer_last_name, writer_id)
    execute_query(query, params)


def delete_writer(writer_id):
    query = "DELETE FROM {} WHERE writer_id = (?)".format(table_name)
    params = (writer_id,)
    execute_query(query, params)
