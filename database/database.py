import sqlite3


class database:

    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query, params, select=None):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()

            if select:
                record_id = cursor.execute(query, params).fetchone()[0]
                return record_id

            cursor.execute(query, params)
            connection.commit()
        except sqlite3.DatabaseError as error:
            print(error)
        finally:
            # noinspection PyUnboundLocalVariable
            cursor.close()
            connection.close()


    # def create_table():


db_name = "movies"
movies_db = database(db_name)