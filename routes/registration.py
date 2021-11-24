from app import app, db
from flask import render_template, request, redirect
from models.models import *


@app.route('/users/new', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user_id = request.form['user_id'],
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email = request.form['email'],
        phone_number = request.form['phone_number'],
        hire_date = request.form['hire_date'],
        login = request.form['login'],
        password = request.form['password']

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
            return redirect('/')
        except:
            return redirect('/error_add')

    else:
        return render_template('main/registration.html')
