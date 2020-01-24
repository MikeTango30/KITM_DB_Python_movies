from database.database import execute_query

table_name = "actors"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                actor_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )""".format(table_name)


def create_actor(actor):
    query = "INSERT INTO {} VALUES(?, ?, ?)".format(table_name)
    params = (actor.actor_id, actor.first_name, actor.last_name)
    actor.actor_id = execute_query(query, params, None, True) # insert and get last inserted id


def read_actor(actor_id):
    query = "SELECT * FROM {} WHERE actor_id = (?)".format(table_name)
    params = (actor_id,)
    execute_query(query, params, True)


def update_name(actor_first_name, actor_id):
    query = "UPDATE {} SET first_name = (?) WHERE actor_id = (?)".format(table_name)
    params = (actor_first_name, actor_id)
    execute_query(query, params)


def update_last_name(actor_last_name, actor_id):
    query = "UPDATE {} SET last_name = (?) WHERE actor_id = (?)".format(table_name)
    params = (actor_last_name, actor_id)
    execute_query(query, params)


def delete_actor(actor_id):
    query = "DELETE FROM {} WHERE actor_id = (?)".format(table_name)
    params = (actor_id,)
    execute_query(query, params)
