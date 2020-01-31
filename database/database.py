import sqlite3

db_name = "movies"


def execute_query(query, params=None, select=None, insert=None):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        if select and params:
            rows = cursor.execute(query, params).fetchall()
            return rows

        if select and not params:
            rows = cursor.execute(query).fetchall()
            return rows

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        connection.commit()

        if insert:
            return cursor.lastrowid

    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        connection.close()
