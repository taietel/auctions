import os

from flask import Flask

from notifications import notifications_bp
from config import Config
from models import db


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(notifications_bp)

    @app.route("/hello")
    def hello():
        return "hello"

    return app
