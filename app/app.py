from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from posts.blueprint import posts_python,posts_flask
from flask_admin import Admin  
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__, static_folder="static")
app.config.from_object(Configuration)

db = SQLAlchemy(app)
app.register_blueprint(posts_flask, url_prefix='/flask')
app.register_blueprint(posts_python, url_prefix='/python')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *
# Admin
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))