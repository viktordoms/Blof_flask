from app import app, db
from flask import render_template
from models.models import Posts


@app.route('/', methods=["GET"])
def main_page():
    post = Posts.query.all()
    return render_template('main.html', post=post)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404

