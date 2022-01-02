import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, '../test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
