#-*- coding:utf-8 -*-

from flask import request, jsonify
from ..auth import authbp

@authbp.route('/login', methods=['GET'])
def login():
    return "login"
