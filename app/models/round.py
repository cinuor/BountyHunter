# -*- coding: utf-8 -*-

from ..models import db
from .base import BaseModel
from .. import utils


class Round(db.Model, BaseModel):
    __tablename__ = 'round'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name

    def __repr__(self):
        return '<Round %r>' % self.name
