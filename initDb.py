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

from faker import Faker
from faker.providers import python
from faker.providers import company

from entities.actor import Actor
from entities.director import Director
from entities.writer import Writer

from movies_repo_json import movies_repo_json
import json

movies_repo = json.dumps(movies_repo_json)

# for item in movies_repo["genres"]:
#     print(item)

for item in movies_repo:
    print(item)
    # for prop in item:
    #     print(prop[0:50])



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
#
# print(fake.pyfloat(3, 2, True, 30, 150))
# print(fake.pyfloat(3, 2, True, 150, 700))
# print(fake.first_name())
# print(fake.last_name())
# print(fake.company() + " Studio")
#
#
# actor = Actor(fake.first_name, fake.last_name)
# actors.create_actor(actor)
# director = Director(fake.first_name, fake.last_name)
# directors.create_director(director)
# writer = Writer(fake.first_name, fake.last_name)
# writers.create_writer(writer)


