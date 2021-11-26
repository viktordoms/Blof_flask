from app import db, manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return 'Users %r>' % self.user_id

    @property
    def serialize(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "login": self.login,
            "password": self.password
        }


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
