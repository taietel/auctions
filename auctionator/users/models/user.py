from werkzeug.security import generate_password_hash, check_password_hash
from auctionator.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.email = email
        self.set_password(password)

    def get_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_by_id(user_id):
        return db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    def __repr__(self):
        return f'<User {self.name!r}>'
