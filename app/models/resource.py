# -*- coding: utf-8 -*-

import string
import enum
from ..models import db
from .base import BaseModel
from .. import utils

__all__ = [
        'Round', 'Investstage', 'Capitaltype', 'Capitalproperty', 
        'Stageproperty', 'Area', 'Currency', 'Tag', 'Industry'
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

class Tag(db.Model, ResourceBase):
    __tablename__ = 'tag'
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, name):
        self.id = utils.generate_uuid()
        self.name = name

class IndustryEnum(enum.Enum):
    Industry = 1
    SegmentIndustry = 2

class Industry(db.Model, BaseModel):
    __tablename__ = 'industry'
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(16), unique=True, nullable=False)
    parentId = db.Column(db.String(36), unique=True, index=True)
    industryType = db.Column(db.Enum(IndustryEnum), nullable=False)

    def __init__(self, name, parentId, industryType):
        self.id = utils.generate_uuid()
        self.name = name
        self.parentId = parentId
        self.industryType = industryType

    def __repr__(self):
        return '<Industry %r>' % self.name if self.industryType == 1 else '<SegmentIndustry %r>' % self.name

    def serialize(self):
        return {
                "id": self.id,
                "name": self.name,
                "parentId": self.parentId,
                "industryType": self.industryType.value
            }
