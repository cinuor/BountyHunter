#-*- coding:utf-8 -*-
from flask import request, make_response, redirect
from flask_restful import Resource
from ..error import *
from ..models.user import User
from .. import utils


__all__ = ["Auth", "SignUp"]

class Auth(Resource):
    def post(self):
        data = utils.get_post_data(request)
        if not data:
            raise BadRequestError(message="No Payload")

        name = data.get('name', None)
        password = data.get('password', None)

        if name is None or password is None:
            raise BadRequestError(message="Parameter Not Found")

        user = User.query.filter_by(name=name).first()
        if user is None:
            raise NotFoundError(message="User Not Found")
        if not utils.validate_password(password, user.password):
            raise UnauthorizedError("Wrong Username Or Password")

        return redirect("/")


class SignUp(Resource):
    def post(self):
        data = utils.get_post_data(request)
        if not data:
            raise BadRequestError(message='No Payload')

        name = data.get('name', None)
        email = data.get('email', None)
        password = data.get('password', None)

        if name is None:
            raise BadRequestError(message='Parameter Not Found')

        password = utils.encrypt_password(password)
        try:
            new_user = User(name, email, password)
            User.add_entry(new_user, True)
        except Exception:
            raise ServerError(message='Cannot Signing Up, Database Error')
        return redirect('/')

