import sqlite3

db_name = "movies"


def execute_query(query, params=None, select=None):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        if select:
            record_id = cursor.execute(query, params).fetchone()[0]
            return record_id

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        connection.commit()
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        connection.close()


    # def create_table():
