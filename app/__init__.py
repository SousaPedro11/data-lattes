from flask import Flask
from flask_bootstrap import Bootstrap

from app.datalattes import datalattes_bp
from config import config


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    Bootstrap(app)

    app.register_blueprint(datalattes_bp)
    return app
