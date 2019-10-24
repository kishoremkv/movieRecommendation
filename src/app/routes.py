from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.models import User
from app.util import get_movie_info_min, get_movie_info, predict, set_preferences, get_preferences
from app.forms import LoginForm, RegistrationForm

from random import randint

import json
import random

movies=[]

@app.route('/')
@login_required
def index():

    result = get_preferences(user_id=current_user.id)
    
    movies = get_movie_info_min(result)
    return render_template('index.html', movies=movies)

@app.route('/movie', methods=['GET'])
@login_required
def movie():

    list = []
    for i in range(1,7):
        list.append(randint(1,45296))
    similar_movies = get_movie_info_min(list)
    

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
        login_user(user)
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

    
@login_required
@app.route('/calibrate',methods=['GET','POST'])
def  calib():

    list1=random.sample(range(1,45296),50)
    if request.method=='GET':
        movies = get_movie_info_min(list1)
        return render_template('calib.html',movies=movies)
    
    if request.method=='POST':
        
        print('submited')

        movshown=[]
        movsel=[]
        
        for i in list1:
            movshown.append(i)
        movsel.extend(request.form.getlist('sel'))
        movsel=[int(i) for i in movsel]
        
        print("\n\n",type(request.form['sel']),"\n\n")
        print("\n\nmovshown:  ",movshown,"\n\n")
        print("\n\nmovsel:  ",movsel,"\n\n")

        movie_ids = predict(movshown,movsel)
        set_preferences(user_id=current_user.id, movie_ids=movie_ids)

        return redirect(url_for('index'))
    
