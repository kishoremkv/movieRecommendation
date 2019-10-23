from app import db
from app.models import User, Movie
from app.util import get_movie_info, get_movie_info_min
import pandas as pd

list = [11,12,13]

movies = get_movie_info_min(list)

print(movies)