from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from .config import Config

db = SQLAlchemy()
api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    api.init_app(app)

    from .routing import ManyMovie, SingleMovie, SingleGenre, ManyGenre

    return app
