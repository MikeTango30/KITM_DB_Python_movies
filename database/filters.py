from database.database import execute_query

movies = "movies"
actors = "actors"
box_offices = "box_offices"
directors = "directors"
genres = "genres"
movies_actors = "movies_actors"
movies_directors = "movies_directors"
movies_genres = "movies_genres"
movies_writers = "movies_writers"
studios = "studios"
types = "types"
writers = "writers"


def get_all_data():
    query = f"""SELECT (movies.title, release_year, runtime, actors.last_name, directors.last_name, writers.last_name, 
                        genres.genre_name, studios.title, boxoffices.overall_sales) 
                FROM {movies}
                JOIN {movies_actors}
                USING (movie_id)
                WHERE actor_id IN(
                    SELECT actor_id
                    FROM {actors} 
                    JOIN {movies_actors} 
                    USING (actor_id))
                JOIN {movies_writers}
                USING (movie_id)
                WHERE writer_id IN(
                    SELECT writer_id
                    FROM {writers} 
                    JOIN {movies_writers} 
                    USING (writer_id)) 
                JOIN {movies_directors}
                USING (movie_id)
                WHERE director_id IN(
                    SELECT director_id
                    FROM {directors} 
                    JOIN {movies_directors} 
                    USING (director_id)) 
                JOIN {movies_genres}
                USING (movie_id) 
                WHERE genre_id IN(
                    SELECT genre_id
                    FROM {genres} 
                    JOIN {movies_genres} 
                    USING (genre_id)) 
                JOIN {studios} 
                USING (movie_id)
                JOIN {box_offices} 
                USING (movie_id)
                GROUP BY movies.title
                """
    return execute_query(query, None, True)


def filter_by_actor(actor_id):
    query = f"""SELECT title, release_year, runtime 
                FROM {movies} JOIN {movies_actors}
                USING (movie_id) 
                WHERE actor_id IN(
                    SELECT actor_id
                    FROM {actors} 
                    JOIN {movies_actors} 
                    USING (actor_id) 
                    WHERE actor_id = ?
                    )"""
    params = (actor_id,)
    return execute_query(query, params, True)


def filter_by_director(director_id):
    query = f"""SELECT title, release_year, runtime 
                FROM {movies} 
                JOIN {movies_directors}
                USING (movie_id) 
                WHERE director_id IN(
                    SELECT director_id
                    FROM {directors} 
                    JOIN {movies_directors} 
                    USING (director_id) 
                    WHERE director_id = ?
                    )"""
    params = (director_id,)
    return execute_query(query, params, True)


def filter_by_writer(writer_id):
    query = f"""SELECT title, release_year, runtime 
                FROM {movies} 
                JOIN {movies_writers}
                USING (movie_id) 
                WHERE writer_id IN(
                    SELECT writer_id
                    FROM {writers} 
                    JOIN {movies_writers} 
                    USING (writer_id) 
                    WHERE writer_id = ?
                    )"""
    params = (writer_id,)
    return execute_query(query, params, True)


def filter_by_genre(genre_id):
    query = f"""SELECT title, release_year, runtime 
                    FROM {movies} 
                    JOIN {movies_genres}
                    USING (movie_id) 
                    WHERE genre_id IN(
                        SELECT genre_id
                        FROM {genres} 
                        JOIN {movies_genres} 
                        USING (genre_id) 
                        WHERE genre_id = ?
                        )"""
    params = (genre_id,)
    return execute_query(query, params, True)


def filter_by_studio(studio_id):
    query = f"""SELECT title, release_year, runtime
                    FROM {movies}
                    JOIN {studios} 
                    USING (movie_id)
                    WHERE studio_id = ?"""
    params = (studio_id,)
    return execute_query(query, params, True)


def filter_by_overall_sales(box_office_id):
    query = f"""SELECT title, release_year, runtime, overall_sales
                    FROM {movies}
                    JOIN {box_offices} 
                    USING (movie_id)
                    WHERE box_office_id = ? ORDER BY overall_sales DESC"""
    params = (box_office_id,)
    return execute_query(query, params, True)


def filter_by_opening_weekend_sales(box_office_id):
    query = f"""SELECT title, release_year, runtime, opening_weekend
                    FROM {movies}
                    JOIN {box_offices} USING (movie_id)
                    WHERE box_office_id = ? ODER BY opening_weekend DESC"""
    params = (box_office_id,)
    return execute_query(query, params, True)


def filter_by_runtime():
    query = """SELECT title, release_year, runtime FROM movies ORDER BY runtime DESC"""
    return execute_query(query, None, True)


def filter_by_rating():
    query = """SELECT title, release_year, runtime FROM movies ORDER BY rating DESC"""
    return execute_query(query, None, True)
