#-*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api

authbp = Blueprint('auth', __name__)

from .auth import *

auth_api = Api(authbp)
auth_api.add_resource(Auth, '/auth/login')
auth_api.add_resource(SignUp, '/signup')

__all__ = ["authbp", "Auth", "SignUp"]
