from database import database


class actor:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS actors (
                                                    actor_id integer PRIMARY KEY,
                                                    first_name text NOT NULL,
                                                    last_name text NOT NULL
                                                    )"""


    def create_actor(self, actor_id=None):
        query = "INSERT INTO hearts VALUES(?, ?, ?)"
        params = (actor_id, self.name, self.lastname)
        database.execute_query(query, params)
