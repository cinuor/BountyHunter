#-*- coding:utf-8 -*-
from flask import Blueprint

auth = Blueprint('auth', __name__)

from BountyHunter.app.auth.auth import *
