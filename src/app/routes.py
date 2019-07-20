from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.models import User, Movie
from app.util import get_movie_info_min
from app.util import get_movie_info

import json
from random import randint




@app.route('/')
@login_required
def index():
    list = []
    for i in range(1,100):
        list.append(randint(1,45296))
    movies = get_movie_info_min(list)
    return render_template('index.html', movies=movies)

@app.route('/movie', methods=['GET'])
@login_required
def movie():

    list = []
    for i in range(1,7):
        list.append(randint(1,45296))
    similar_movies = get_movie_info_min(list)
    print(similar_movies[2].poster_path_w154)

    movie_id = request.args.get('id')
    movie = get_movie_info(movie_id)
    return render_template('movie.html', movie=movie, similar_movies=similar_movies)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['login_email']).first()
        
        if user is None or not user.check_password(request.form['login_password']):
            error = 'Invalid email or password'
            return redirect('/login')
        login_user(user)
        return redirect('/')

    return render_template('login.html')
