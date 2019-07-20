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
        list.append(randint(1,45467))
    movies = get_movie_info_min(list)
    print(movies[2].original_title)
    return render_template('index.html', movies=movies)

@app.route('/movie', methods=['GET'])
@login_required
def movie():
    movie_id = request.args.get('id')
    movie = get_movie_info(movie_id)
    return render_template('movie.html', movie=movie)


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
        
        if user is None or not user.check_password('admin'):
            error = 'Invalid email or password'
            return redirect('/login')
        login_user(user)
        return redirect('/')

    return render_template('login.html')
