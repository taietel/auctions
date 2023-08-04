from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
API_KEY = environ.get("API_KEY")
DB_NAME = environ.get("DB_NAME")
DB_USER = environ.get("DB_USER")
DB_PASSWORD = environ.get("DB_PASSWORD")
