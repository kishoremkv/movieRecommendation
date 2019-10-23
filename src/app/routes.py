from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.models import User, Movie
from app.util import get_movie_info_min
from app.util import get_movie_info
from app.forms import LoginForm, RegistrationForm

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
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)   

    
