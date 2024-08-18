from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/<name>")
def get_name(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello')
def hello():
    return 'Hello, World'
