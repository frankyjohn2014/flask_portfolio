from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from posts.blueprint import posts_python,posts_flask


app = Flask(__name__, static_folder="static")
app.config.from_object(Configuration)

db = SQLAlchemy(app)
app.register_blueprint(posts_flask, url_prefix='/flask')
app.register_blueprint(posts_python, url_prefix='/python')
