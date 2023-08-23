import os
from dotenv import load_dotenv
from flask import Flask
from auctionator.database import init_db
from auctionator import views

load_dotenv("../.env")


def add_views(app):
    for view in views:
        app.register_blueprint(view)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.from_mapping(test_config)

    add_views(app)
    init_db(app)

    return app
