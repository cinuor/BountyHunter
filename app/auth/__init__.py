#-*- coding:utf-8 -*-
from flask import Blueprint

authbp = Blueprint('auth', __name__)

from .auth import *
