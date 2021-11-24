from app import app
from flask import render_template


@app.route('/', methods=["GET"])
def main_page():
    return render_template('main/main.html')


@app.route('/users/exit', methods=["GET"])
def main_page():
    return render_template('main/authorization.html')


@app.route('/users/new', methods=["GET"])
def main_page():
    return render_template('main/registration.html')
