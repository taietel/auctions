from auctionator.users.models import User
from auctionator.database import db


def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user


def get_user(username):
    return db.session.query(User).filter_by(username=username).first()


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return False

    return user.get_json()


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_all_users():
    return User.query.all()


def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users
