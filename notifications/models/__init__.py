
from flask_sqlalchemy import SQLAlchemy
from models import db


# __all__ = ["Product", "Category"]


def init_app(app):
    db.init_app(app)
