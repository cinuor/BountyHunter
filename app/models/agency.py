# -*- coding: utf-8 -*-
from ..models import db
from .base import BaseModel
from .. import utils

class Agency(db.Model, BaseModel):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(40), unique=True, nullable=False)
    fullname = db.Column(db.String(80))
    nickname = db.Column(db.String(40))
    website = db.Column(db.String(64))
    capitalType = db.Column(db.String(20), nullable=False)
    capitalProperty = db.Column(db.String(20), nullable=False)
    stageProperty = db.Column(db.String(20), nullable=False)
    upperLimit = db.Column(db.Integer, nullable=False)
    lowerLimit = db.Column(db.Integer, nullable=False)

    def __init__(self, name, fullname, nickname, website, capitalType,
            capitalProperty, stageProperty, upperLimit, lowerLimit):
        self.id = utils.generate_uuid()
        self.name = name
        self.fullname = fullname
        self.nickname = nickname
        self.website = website
        self.capitalType = capitalType
        self.capitalProperty = capitalProperty
        self.stageProperty = stageProperty
        self.upperLimit = upperLimit
        self.lowerLimit = lowerLimit

    def __repr__(self):
        return '<Agency %r>' % self.name
