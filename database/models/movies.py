from database.database import execute_query

table_name = "movies"


def create_movies_table():
    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                                movie_id integer PRIMARY KEY,
                                                title text NOT NULL,
                                                rating decimal NOT NULL,
                                                runtime time NOT NULL,
                                                release_year text NOT NULL
                                                )"""
    execute_query(query)


def create_movie(movie):
    query = f"INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?)"
    params = (movie.movie_id, movie.title, movie.rating, movie.runtime, movie.release_year)
    movie.movie_id = execute_query(query, params, None, True)


def read_movie(movie_id):
    query = f"SELECT * FROM {table_name} WHERE movie_id = (?)"
    params = (movie_id,)
    execute_query(query, params, True)


def update_title(movie_id, movie_title):
    query = f"UPDATE {table_name} SET title = (?) WHERE movie_id = (?)"
    params = (movie_title, movie_id)
    execute_query(query, params)


def update_rating(movie_id, movie_rating):
    query = f"UPDATE {table_name} SET rating = (?) WHERE movie_id = (?)"
    params = (movie_rating, movie_id)
    execute_query(query, params)


def update_runtime(movie_id, movie_runtime):
    query = f"UPDATE {table_name} SET runtime = (?) WHERE movie_id = (?)"
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
