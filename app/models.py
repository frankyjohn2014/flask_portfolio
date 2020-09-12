from app import db
import re
import datetime
from flask_security import UserMixin, RoleMixin

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

post_category = db.Table('post_category',
                        db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                        db.Column('category_id', db.Integer, db.ForeignKey('category.id')))

import os.path as op

def thumb_name(filename):
    name, _ = op.splitext(filename)
    return   secure_filename('%s-thumb.jpg' % name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description =  db.Column(db.String(140))
    url_site = db.Column(db.String(140))
    categorys = db.relationship('Category', secondary=post_category, backref=db.backref('posts', lazy='dynamic'))
    path = db.Column(db.Unicode(128))
    type = db.Column(db.Unicode(3)) 
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()

# Если нужен слаг
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return 'id:{}\n title: {}'.format(self.id, self.title)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug =  db.Column(db.String(140), unique=True)
    path = db.Column(db.Unicode(128))
    type = db.Column(db.Unicode(3)) 
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()



    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        # return 'id:{}, title: {}'.format(self.id, self.title)
        return self.title



roles_users = db.Table('roles_users',
                        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                        ) 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary = roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
