# -*- coding: UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from BountyHunter.app.auth import auth as auth_blueprint
#from BountyHunter.config import config

from app.auth import authbp as auth_blueprint

db = SQLAlchemy()

def create_app(config_name, config):
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    app.config.from_object(config[config_name])
    return app
