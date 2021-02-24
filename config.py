import os


class Config:
    THREADED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)


class Devlopment(Config):
    DEBUG = os.environ.get('FLASK_DEBUG', False)


class Production(Config):
    pass


config = {
    'dev': Devlopment,
    'prod': Production,
}
