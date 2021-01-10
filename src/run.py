from flask import Flask
from src.settings import Settings
from flask_pymongo import PyMongo


def create_app(config_class=Settings):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)
    flask_app.logger.info('Created app')
    return flask_app


app = create_app()
mongo = PyMongo(app)

import src.recommendator.controller  # Imports recommendator routes
