import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv("../.env")

from auctionator.notifications import notifications_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(notifications_bp)

    return app
