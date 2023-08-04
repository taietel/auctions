import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv("../.env")


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_pyfile("../config.py")
    else:
        app.config.from_mapping(test_config)

    @app.route("/")
    def index():
        return f'SECRET_KEY = { app.config.get("SECRET_KEY") }'

    from . import db

    db.init_app(app)
    # from . import auth

    # app.register_blueprint(auth.bp)

    return app
