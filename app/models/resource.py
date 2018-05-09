# -*- coding: utf-8 -*-

import string
from ..models import db
from .base import BaseModel
from .. import utils

__all__ = [
        'Round', 'Investstage', 'Capitaltype', 'Capitalproperty', 
        'Stageproperty', 'Area', 'Currency'
    ]

class ResourceBase(BaseModel):

    def __repr__(self):
        return '<%s %s>'.format(self.__entryname__, self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Round(db.Model, ResourceBase):
    __tablename__ = 'round'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name


class Investstage(db.Model, ResourceBase):
    __tablename__ = 'investstage'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name


class Capitaltype(db.Model, ResourceBase):
    __tablename__ = 'capitaltype'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name

class Capitalproperty(db.Model, ResourceBase):
    __tablename__ = 'capitalproperty'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name


class Stageproperty(db.Model, ResourceBase):
    __tablename__ = 'stageproperty'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name

class Area(db.Model, ResourceBase):
    __tablename__ = 'area'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name

class Currency(db.Model, ResourceBase):
    __tablename__ = 'currency'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name
