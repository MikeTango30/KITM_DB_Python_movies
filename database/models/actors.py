from database.database import execute_query

table_name = "actors"


def create_actors_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                actor_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )"""
    execute_query(query)


def create_actor(actor):
    query = f"INSERT INTO {table_name} VALUES(?, ?, ?)"
    params = (actor.actor_id, actor.first_name, actor.last_name)
    actor.actor_id = execute_query(query, params, None, True)  # insert and get last inserted id


def read_actor(actor_id):
    query = f"SELECT * FROM {table_name} WHERE actor_id = (?)"
    params = (actor_id,)
    execute_query(query, params, True)


def update_name(actor_first_name, actor_id):
    query = f"UPDATE {table_name} SET first_name = (?) WHERE actor_id = (?)"
    params = (actor_first_name, actor_id)
    execute_query(query, params)


def update_last_name(actor_last_name, actor_id):
    query = f"UPDATE {table_name} SET last_name = (?) WHERE actor_id = (?)"
    params = (actor_last_name, actor_id)
    execute_query(query, params)


def delete_actor(actor_id):
    query = f"DELETE FROM {table_name} WHERE actor_id = (?)"
    params = (actor_id,)
    execute_query(query, params)
