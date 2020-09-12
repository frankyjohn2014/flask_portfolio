from app import app
from flask import render_template
from models import Category, Post



@app.route('/')
def index():
    categorys = Category.query.all()
    return render_template('index.html', categorys=categorys)


@app.route('/<slug>')
def category_detail(slug):
    posts = ''
    category = Category.query.filter(Category.slug==slug).first_or_404()
    try:
        posts = category.posts.all()
    except:
        pass
    return render_template('category_detail.html', category=category, posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404