from flask import Blueprint
from flask import render_template

posts_python = Blueprint('posts_python', __name__, template_folder='templates')
posts_flask = Blueprint('posts_flask', __name__, template_folder='templates')

@posts_python.route('/')
def python():
    return render_template('posts_python/python.html')

@posts_flask.route('/')
def flask():
    return render_template('posts_flask/flask.html')