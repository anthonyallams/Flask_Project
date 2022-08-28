from flask import Flask, jsonify
import psycopg2, psycopg2.extras
from settings import DB_NAME, DB_USER, DB_PASSWORD

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
    movies_records = cursor.fetchall()
    return jsonify(movies_records)

@app.route('/movies/<int:id>')
def movie(id):
    cursor = db_connect()
    cursor.execute('SELECT * FROM movies WHERE id = %s',(id,))
    movies_record = cursor.fetchone()
    return jsonify(movies_record)
    
@app.route('/ratings')
def ratings():
    cursor = db_connect()
    cursor.execute('SELECT * FROM ratings;')
    ratings_records = cursor.fetchall()
    return jsonify(ratings_records)

@app.route('/ratings/<int:id>')
def rating(id):
    cursor = db_connect()
    cursor.execute('SELECT * FROM ratings WHERE id = %s',(id,))
    ratings_record = cursor.fetchone()
    return jsonify(ratings_record)


app.run(debug=True)