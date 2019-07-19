# # serve.py
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# from flask import render_template, redirect, url_for, request

# # creates a Flask application, named app
# app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
    
#     error = None
#     if request.method == 'POST':
#         if request.form['login_email'] != 'admin' or request.form['login_password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect('/')
#     return render_template('login.html', error=error)

# # a route where we will display a welcome message via an HTML template
# @app.route("/")
# def hello():
#     movies = [
#         {
#             'title': 'Toy Story Toy Story Toy Story Toy Story Toy Story Toy Story',
#             'year': '1995',
#             'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
#         },
#         {
#             'title': 'Toy Story',
#             'year': '1995',
#             'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
#         },
#         {
#             'title': 'Toy Story',
#             'year': '1995',
#             'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
#         },
#         {
#             'title': 'Toy Story',
#             'year': '1995',
#             'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
#         },
#     ]
#     return render_template('index.html', movies=movies)

# # run the application
# if __name__ == "__main__":
#     app.run(debug=True)
#     app.config.from_object(Config)
#     db = SQLAlchemy(app)

from app import app