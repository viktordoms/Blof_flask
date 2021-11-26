from flask import render_template, request, redirect, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user

# @login_required трібно прописати під роутами де можуть заходити тільки авторизовані користувачі

from models.models import Users
from app import app


@app.route('/users/exit', methods=["GET", "POST"])
def authorization():
    login = request.form.get("login")
    password = request.form.get("password")

    if login and password:
        user = Users.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page)
        else:
            flash("Помилка.Заповніть логін або пароль")
    else:
        flash("Помилка.Перевірте логін або пароль")
    return render_template('main/authorization.html')


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.after_request
def redirect_to_registration(response):
    if response.status_code == 401:
        return redirect("/users/new" + "?next" + request.url)

    return response
