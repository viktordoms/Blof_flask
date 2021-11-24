from app import app, db
from flask import render_template, request, redirect,flash
from models.models import *


@app.route('/users/new', methods=['POST', 'GET'])
def registration():
    user_id = request.form.get('user_id')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    hire_date = request.form.get('hire_date')
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (user_id or first_name or last_name or email or phone_number or hire_date
                or login or password or password2):
            flash("Заповніть всі поля")
        elif password != password2:
            flash("Паролі не співпадають")
        else:
            user = Users(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                hire_date=hire_date,
                login=login,
                password=password
            )
            try:
                db.session.add(user)
                db.session.commit()
                return redirect('/users/exit')
            except:
                return redirect('/error_add')

    else:
        return render_template('main/registration.html')
