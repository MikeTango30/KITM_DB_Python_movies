from database.database import execute_query

table_name = "actors"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                actor_id integer PRIMARY KEY,
                                                first_name text NOT NULL,
                                                last_name text NOT NULL
                                                )""".format(table_name)


def create_actor(actor, actor_id=None):
    query = "INSERT INTO {} VALUES(?, ?, ?)".format(table_name)
    params = (actor_id, actor.name, actor.lastname)
    execute_query(query, params)
