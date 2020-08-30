from app import db
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

post_category = db.Table('post_category',
                        db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                        db.Column('category_id', db.Integer, db.ForeignKey('category.id')))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug =  db.Column(db.String(140), unique=True)
    url_site = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()
    
    categorys = db.relationship('Category', secondary=post_category, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Tag id:{}, title: {}>'.format(self.id, self.title)
    


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug =  db.Column(db.String(140), unique=True)


    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.generate_slug()



    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Tag id:{}, title: {}>'.format(self.id, self.title)
    
