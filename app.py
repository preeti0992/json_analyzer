from flask import Flask, render_template
from json_player import *

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Index Page'
    return load_json('sample_array.json')


@app.route('/attributes')
def attributes():
    data = load_json('sample_array.json')
    return load_all_attributes(data)


@app.route('/attributes2')
def attributes2():
    data = load_json('sample.json')
    return load_all_attributes(data)


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)