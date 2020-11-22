from flask import Flask
from json_player import *

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Index Page'
    return load_json()


@app.route('/hello')
def hello():
    return 'Hello, World'
