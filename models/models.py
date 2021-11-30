from app import db
from flask_login import UserMixin
from datetime import datetime


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return 'Users %r>' % self.id

    @property
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }



class Posts(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    categor = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Posts %r>' % self.post_id

    @property
    def serialize(self):
        return {
            "post_id": self.post_id,
            "categor": self.categor,
            "topic": self.topic,
            "text": self.text,
            "date_add": self.date_add
        }
