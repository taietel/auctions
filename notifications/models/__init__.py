from .category import Category
from .product import Product
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


__all__ = ["Product", "Category"]


def init_app(app):
    db.init_app(app)
