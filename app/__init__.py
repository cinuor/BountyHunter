# -*- coding: UTF-8 -*-
from flask import Flask, jsonify
from app.auth import authbp
from app import error, utils

def create_app(config_name, config):
    app = Flask(__name__)
    app.register_blueprint(authbp)
    app.config.from_object(config[config_name])
    register_errorhandler(app)
    return app

def error_handler(error):
    resp = jsonify(error.to_dict())
    resp.status_code = error.status_code
    return resp

def register_errorhandler(app):
    for name in error.__all__:
        c = getattr(error, name)
        app.register_error_handler(c, error_handler)
