from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config.from_object("config.Config")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.init_app(app)

with app.app_context():
     from routes.main import *


     db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
