from database.filters import get_all_data
from database.filters import filter_by_actor
from database.filters import filter_by_director
from database.filters import filter_by_writer
from database.filters import filter_by_genre

from database.models import actors
from database.models import box_offices
from database.models import directors
from database.models import genres
from database.models import movies
from database.models import movies_actors
from database.models import movies_directors
from database.models import movies_genres
from database.models import movies_writers
from database.models import studios
from database.models import writers
import random

from faker import Faker
from faker.providers import python
from faker.providers import company

from entities.actor import Actor
from entities.director import Director
from entities.writer import Writer
from entities.genre import Genre
from entities.studio import Studio
from entities.box_office import Box_office
from entities.movie import Movie

from movies_repo import movies_repo


# print(movies_repo["movies"][0]["title"])
# for item in movies_repo["movies"]:
#     for k, v in item.items():
#         if k == "title" or k == "runtime" or k == "year":
#             print(k + " " + v)

# actors.create_actors_table()
# box_offices.create_box_offices_table()
# directors.create_directors_table()
# genres.create_genres_table()
# movies.create_movies_table()
# movies_writers.create_movies_writers_table()
# movies_genres.create_movies_genres_table()
# movies_directors.create_movies_directors_table()
# movies_actors.create_movies_actors_table()
# studios.create_studios_table()
# writers.create_writers_table()
#
#
# fake = Faker()
# fake.add_provider(python)
# fake.add_provider(company)

# # fake actors, directors, writers
# for i in range(500):
#     actor = Actor(fake.first_name(), fake.last_name())
#     actors.create_actor(actor)
#     director = Director(fake.first_name(), fake.last_name())
#     directors.create_director(director)
#     writer = Writer(fake.first_name(), fake.last_name())
#     writers.create_writer(writer)
#
# random.seed()
# # fake studios
# for i in range(50):
#     studio = Studio(fake.company() + " Studio")
#     studios.create_studio(studio, random.randrange(1, 147))
#
# # make genres
# for i in movies_repo["genres"]:
#     genre = Genre(i)
#     genres.create_genre(genre)

# # fake box offices
# for i in range(147):
#     box_office = Box_office(fake.pyfloat(3, 2, True, 30, 150), fake.pyfloat(3, 2, True, 150, 700))
#     box_offices.create_box_office(box_office, random.randrange(1, 147))

# fake movies actors, directors, writers relationships
# for i in range(500):
#     movies_actors.create_relationship(random.randrange(1, 147), random.randrange(1, 501))
#     movies_writers.create_relationship(random.randrange(1, 147), random.randrange(1, 501))
#     movies_directors.create_relationship(random.randrange(1, 147), random.randrange(1, 501))

# fake movies genre relationships
# for i in range(147):
#     movies_genres.create_relationship(random.randrange(1, 147), random.randrange(1, len(movies_repo["genres"])))

# titles = []
# runtimes = []
# years = []
# for item in movies_repo["movies"]:
#     for k, v in item.items():
#         if k == "title":
#             titles.append(v)
#         if k == "runtime":
#             runtimes.append(v)
#         if k == "year":
#             years.append(v)
#
# for title, runtime, year in zip(iter(titles), iter(runtimes), iter(years)):
#     movie = Movie(title, random.random()*10, runtime, year)
#     movies.create_movie(movie)

rows = get_all_data()
for row in rows:
    print(row)

