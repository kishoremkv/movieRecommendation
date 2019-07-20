import pandas as pd
from random import randint
from app.models import Movie
import os

path = os.getcwd() + '/app/dataset/movies_metadata.csv'
data = pd.read_csv(path)
def get_movie_info_min(list):
    movies = []
    for index in list:
        movies.append(Movie(id=index, original_title=data.loc[index,'original_title'], release_date=data.loc[index,'release_date'], poster_path=data.loc[index,'poster_path']))
    return movies

def get_movie_info(id):

    id = int(id)
    movie = Movie( 
        id=id,
        original_title=data.loc[id,'original_title'],
        poster_path=data.loc[id,'poster_path'], 
        release_date=data.loc[id,'release_date'],
        adult=data.loc[id,'adult'],
        genres=data.loc[id,'genres'],
        imdb_id=data.loc[id,'imdb_id'],
        original_language=data.loc[id,'original_language'],
        overview=data.loc[id,'overview'],
        production_companies=data.loc[id,'production_companies'],
        runtime=data.loc[id,'runtime']
    )
    print(movie)
    return movie