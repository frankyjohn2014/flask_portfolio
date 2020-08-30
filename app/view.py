from app import app
from flask import render_template
from models import Category, Post

@app.route('/', methods=['GET','POST'])
def index():
    categorys = Category.query.all()
    return render_template('index.html', categorys=categorys)


@app.route('/<slug>')
def category_detail(slug):
    category = Category.query.filter(Category.slug==slug).first()
    category_posts = Post.query.filter(Category.slug==slug).first()
    posts = category_posts.query.all()
    return render_template('category_detail.html', category=category, posts=posts)
