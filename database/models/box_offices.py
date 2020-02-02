from database.database import execute_query

table_name = "box_offices"


def create_box_offices_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                box_office_id integer PRIMARY KEY,
                                                movie_id integer,
                                                opening_weekend decimal NOT NULL,
                                                overall_sales decimal NOT NULL,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
                                                ON UPDATE CASCADE
                                                ON DELETE CASCADE
                                                )"""
    execute_query(query)


def create_box_office(box_office, movie_id):
    query = f"INSERT INTO {table_name} VALUES(?, ?, ?, ?)"
    params = (box_office.box_office_id, movie_id, box_office.opening_weekend, box_office.overall)
    box_office.box_office_id = execute_query(query, params, None, True)


def read_box_office(box_office_id):
    query = f"SELECT * FROM {table_name} WHERE box_office_id = (?)"
    params = (box_office_id,)
    execute_query(query, params, True)


def update_movie_id(movie_id, box_office_id):
    query = f"UPDATE {table_name} SET movie_id = (?) WHERE box_office_id = (?)"
    params = (movie_id, box_office_id)
    execute_query(query, params)


def update_opening_weekend(box_office_opening_weekend, box_office_id):
    query = f"UPDATE {table_name} SET opening_weekend = (?) WHERE box_office_id = (?)"
    params = (box_office_opening_weekend, box_office_id)
    execute_query(query, params)


def update_overall_sales(box_office_overall_sales, box_office_id):
    query = f"UPDATE {table_name} SET overall_sales = (?) WHERE box_office_id = (?)"
    params = (box_office_overall_sales, box_office_id)
    execute_query(query, params)


def delete_box_office(box_office_id):
    query = f"DELETE FROM {table_name} WHERE box_office_id = (?)"
    params = (box_office_id,)
    execute_query(query, params)
