from database.database import execute_query

table_name = "movies"


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS {} (
                                                movie_id integer PRIMARY KEY,
                                                title text NOT NULL,
                                                rating decimal NOT NULL,
                                                runtime time NOT NULL,
                                                release_year text NOT NULL
                                                )""".format(table_name)
    execute_query(query)


def create_movie(movie):
    query = "INSERT INTO {} VALUES(?, ?, ?, ?, ?)".format(table_name)
    params = (movie.movie_id, movie.title, movie.rating, movie.runtime, movie.release_year)
    movie.movie_id = execute_query(query, params, None, True)


def read_movie(movie_id):
    query = "SELECT * FROM {} WHERE movie_id = (?)".format(table_name)
    params = (movie_id,)
    execute_query(query, params, True)


def update_title(movie_id, movie_title):
    query = "UPDATE {} SET title = (?) WHERE movie_id = (?)".format(table_name)
    params = (movie_title, movie_id)
    execute_query(query, params)


def update_rating(movie_id, movie_rating):
    query = "UPDATE {} SET rating = (?) WHERE movie_id = (?)".format(table_name)
    params = (movie_rating, movie_id)
    execute_query(query, params)


def update_runtime(movie_id, movie_runtime):
    query = "UPDATE {} SET runtime = (?) WHERE movie_id = (?)".format(table_name)
    params = (movie_runtime, movie_id)
    execute_query(query, params)


def update_release_year(movie_id, movie_release_year):
    query = "UPDATE {} SET release_year = (?) WHERE movie_id = (?)".format(table_name)
    params = (movie_release_year, movie_id)
    execute_query(query, params)


def delete_movie(movie_id):
    query = "DELETE FROM {} WHERE movie_id = (?)".format(table_name)
    params = (movie_id,)
    execute_query(query, params)
