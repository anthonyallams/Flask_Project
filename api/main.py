from flask import Flask, jsonify
import psycopg2, psycopg2.extras
from settings import DB_NAME, DB_USER, DB_PASSWORD
from movies import Movie
from ratings import Rating

app = Flask(__name__)

app.config.update(
    DATABASE=DB_NAME,
    USERNAME=DB_USER,
    PASSWORD=DB_PASSWORD
)

def db_connect():
     conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USERNAME'], password = app.config['PASSWORD'])
     cursor = conn.cursor()
     return cursor 

@app.route('/')
def home():
    return '<h1>Welcome to Movies Recommendation site</h1>'

@app.route('/movies')
def movies():
    cursor = db_connect()
    cursor.execute('SELECT * FROM movies;')
    data_response = cursor.fetchall()
    movies = [Movie(movie) for movie in data_response]
    movie_dicts = [movie.__dict__ for movie in movies]
    return jsonify(movie_dicts)

@app.route('/movies/<int:id>')
def movie(id):
    cursor = db_connect()
    cursor.execute('SELECT * FROM movies WHERE id = %s',(id,))
    data_response = cursor.fetchone()
    movie_details = Movie(data_response)
    movie = movie_details.__dict__
    return jsonify(movie)
    
@app.route('/ratings')
def ratings():
    cursor = db_connect()
    cursor.execute('SELECT * FROM ratings limit 100;')
    data_response = cursor.fetchall()
    ratings = [Rating(rating) for rating in data_response]
    ratings_dict = [rating.__dict__ for rating in ratings]
    return jsonify(ratings_dict)

@app.route('/ratings/<int:id>')
def rating(id):
    cursor = db_connect()
    cursor.execute('SELECT * FROM ratings WHERE id = %s',(id,))
    ratings_record = cursor.fetchone()
    rating_details = Rating(ratings_record)
    rating = rating_details.__dict__
    return jsonify(rating)


app.run(debug=True)