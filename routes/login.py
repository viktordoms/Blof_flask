from flask import flash, redirect, request, url_for, session, abort
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from models.models import Users
from app import app, login_manager
from routes.main import *


@app.route('/users/exit', methods=["GET", "POST"])
def login():
     email = request.form.get("email")
     password = request.form.get("password")

     if email and password:
         user = Users.query.filter_by(email=email).first()
         if user and check_password_hash(user.password, password):
             login_user(user)
             # next_page = request.args.get("next")
             flash('Авторизація успішна')
             return redirect('/')
         else:
             flash("Помилка.Перевірте логін або пароль")
             return redirect(url_for("login"))
     else:
         return render_template('login.html')


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Для створення поста потрібно бути авторизованим")
    return redirect(url_for('main_page'))


@app.after_request
def redirect_to_singin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + "?next" + request.url)
    return response


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


@app.route("/users/<id>")
def user(id):
    if "userLogged" not in session or session['userLogged'] != id:
        abort(401)

    return f"Профіль #: {id}"
