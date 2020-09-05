from flask import Flask, url_for, Markup
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
from flask_admin.contrib import sqla
from flask_admin import form

import random
import os


class StorageAdminModel(sqla.ModelView):

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        url = url_for('static', filename=os.path.join('', model.path))

        if model.type in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup('<img src="%s" width="100">' % url)

        if model.type in ['mp3']:
            return Markup('<audio controls="controls"><source src="%s" type="audio/mpeg" /></audio>' % url)

    column_formatters = {
        'path': _list_thumbnail
    }
    # переопределил внутри base_path to 'static' было base_path
    form_extra_fields = {
        'file': form.FileUploadField('file')
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                path = '%s.%s' % (hash, ext)

                storage_file.save(
                   os.path.join(app.config['STORAGE'], path)
                )

                # _form.name.data = _form.name.data or storage_file.filename
                _form.path.data = path
                # _form.type.data = ext

                del _form.file

        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_path_data(
            super(StorageAdminModel, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_path_data(
            super(StorageAdminModel, self).create_form(obj)
        )


admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(StorageAdminModel(Category, db.session))
# admin.add_view(ModelView(Category, db.session))