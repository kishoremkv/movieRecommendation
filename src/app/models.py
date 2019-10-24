from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserPreferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Movie():
    def __init__(
            self=None, 
            id=None, 
            original_title=None, 
            poster_path_w154=None,
            poster_path_w500=None,
            poster_path=None, 
            release_date=None,
            adult=None,
            belongs_to_collection=None,
            budget=None,
            genres=None,
            homepage=None,
            imdb_id=None,
            original_language=None,
            overview=None,
            popularity=None,
            production_companies=None,
            production_countries=None,
            revenue=None,
            runtime=None,
            spoken_languages=None,
            status=None,
            tagline=None,
            title=None,
            video=None,
            vote_average=None,
            vote_count=None,
            cast=None
        ):  
        self.id = id
        self.original_title = original_title
        self.poster_path_w154 = 'http://image.tmdb.org/t/p/w154{}'.format(poster_path)
        self.poster_path_w500 = 'http://image.tmdb.org/t/p/w500{}'.format(poster_path)
        self.release_date = str(release_date)[-4:]
        self.adult = adult  
        self.belongs_to_collection = belongs_to_collection
        self.budget = budget
        self.genres = genres
        self.homepage = genres
        self.imdb_id = imdb_id 
        self.original_language = original_language
        self.overview = overview
        self.popularity = popularity
        self.production_companies = production_companies
        self.production_countries = production_countries
        self.revenue = revenue
        if runtime is not None:
            hours = int(runtime/60)
            minutes = int(runtime%60)
            self.runtime = '{} hr {} min'.format(hours, minutes)
        
        self.spoken_languages = spoken_languages
        self.status = status
        self.tagline = tagline
        self.title = title
        self.video = video
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.cast = cast
   
