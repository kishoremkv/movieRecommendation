# serve.py

from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    movies = [
        {
            'title': 'Toy Story',
            'year': '2001',
            'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
        },
        {
            'title': 'Toy Story',
            'year': '2001',
            'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
        },
        {
            'title': 'Toy Story',
            'year': '2001',
            'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
        },
        {
            'title': 'Toy Story',
            'year': '2001',
            'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
        },
        {
            'title': 'Toy Story',
            'year': '2001',
            'poster': 'https://image.tmdb.org/t/p/w500/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
        }
    ]
    return render_template('index.html', movies=movies)

# run the application
if __name__ == "__main__":
    app.run(debug=True)