from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def get_migrate(app):
    return Migrate(app, db)


def create_db():
    db.create_all()


def init_db(app):
    import auctionator.users.models.user
    db.init_app(app)


