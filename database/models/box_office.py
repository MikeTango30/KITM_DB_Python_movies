from database.database import execute_query

table_name = "box_offices"


def create_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                box_office_id integer PRIMARY KEY,
                                                movie_id integer
                                                opening_weekend decimal NOT NULL,
                                                overall_sales decimal NOT NULL,
                                                FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
                                                ON UPDATE CASCADE,
                                                ON DELETE CASCADE
                                                )""".format(table_name)
    execute_query(query)


def create_box_office(box_office, movie_id):
    query = "INSERT INTO {} VALUES(?, ?, ?, ?)".format(table_name)
    params = (box_office.box_office_id, movie_id, box_office.opening_weekend, box_office.overall)
    box_office.box_office_id = execute_query(query, params, None, True)


def read_box_office(box_office_id):
    query = "SELECT * FROM {} WHERE box_office_id = (?)".format(table_name)
    params = (box_office_id,)
    execute_query(query, params, True)


def update_movie_id(movie_id, box_office_id):
    query = "UPDATE {} SET movie_id = (?) WHERE box_office_id = (?)".format(table_name)
    params = (movie_id, box_office_id)
    execute_query(query, params)


def update_opening_weekend(box_office_opening_weekend, box_office_id):
    query = "UPDATE {} SET opening_weekend = (?) WHERE box_office_id = (?)".format(table_name)
    params = (box_office_opening_weekend, box_office_id)
    execute_query(query, params)


def update_overall_sales(box_office_overall_sales, box_office_id):
    query = "UPDATE {} SET overall_sales = (?) WHERE box_office_id = (?)".format(table_name)
    params = (box_office_overall_sales, box_office_id)
    execute_query(query, params)


def delete_box_office(box_office_id):
    query = "DELETE FROM {} WHERE box_office_id = (?)".format(table_name)
    params = (box_office_id,)
    execute_query(query, params)
