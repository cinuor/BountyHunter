#-*- coding:utf-8 -*-
from flask import request, jsonify
from BountyHunter.app.auth import auth

@auth.route('/login', methods=['GET'])
def login():
    return "login"
