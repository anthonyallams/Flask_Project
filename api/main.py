from flask import Flask, jsonify
import psycopg2, psycopg2.extras
from settings import DB_NAME, DB_USER, DB_PASSWORD

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=DB_NAME,
    USERNAME=DB_USER,
    PASSWORD=DB_PASSWORD
)

def db_connect():
     conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USERNAME'], password = app.config['PASSWORD'])
     cursor = conn.cursor()
     return cursor 