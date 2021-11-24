from app import app
from flask import render_template


@app.route('/', methods=["GET"])
def main_page():
    return render_template('main/main.html')


@app.route('/error_add')
def error_add():
    return render_template('error_add.html')
