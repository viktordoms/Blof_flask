from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
api = Api(app)
app.config.from_object("config.Config")
app.config['SECRET_KEY'] = "59ceec65a970fa3b1a00830e53081eb6f565c272"
manager = LoginManager(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

with app.app_context():
     from routes.main import *
     from routes.registration import *
     from routes.authorization import *

     db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
