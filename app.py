from flask import Flask
from dotenv import load_dotenv

load_dotenv(".env")


class ActionApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_pyfile("config.py")


if __name__ == '__main__':
    auctions_app = ActionApp()
    auctions_app.app.run()
