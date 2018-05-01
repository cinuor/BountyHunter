# -*- coding: utf-8 -*-
from ..models import db
from .base import BaseModel
from .. import utils

class User(db.Model, BaseModel):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(44), nullable=False)

    def __init__(self, name, email, password):
        self.id = utils.generate_uuid()
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name
