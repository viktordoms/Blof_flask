from app import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer)
    hire_date = db.Column(db.String(50))
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Users %r>' % self.user_id

    @property
    def serialize(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "hire_date": self.hire_date,
            "login": self.login,
            "password": self.password
        }
