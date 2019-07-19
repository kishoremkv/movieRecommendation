from app import db
from app.models import User, Movie
import pandas as pd


# User.query.filter(User.id == 1).delete()
# db.session.commit()

# u = User(email='admin')
# u.set_password('admin')
# db.session.add(u)
# db.session.commit()

data = pd.read_csv('D:\projects\movie-recommendation\dataset\movies_metadata.csv')
print(data.head())
 
movies = []
for i in range(1,10):
    movies.append(Movie(title=data.loc[i,'original_title'], release_date='1995', poster_path="https://image.tmdb.org/t/p/w500".format(data.loc[i,'poster_path'])))

print(movies)    