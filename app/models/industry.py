# -*- coding: utf-8 -*-

import enum
from ..models import db
from .base import BaseModel
from .. import utils

class IndustyEnum(enum.Enum):
    Industry = 1
    SegmentIndustry = 2

class Industry(db.Model, BaseModel):
    __tablename__ = 'industry'
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(16), unique=True, nullable=False)
    parentId = db.Column(db.String(36), unique=True, index=True)
    industyType = db.Column(db.Enum(IndustyEnum), nullable=False)

    def __init__(self, name, parentId, industyType):
        self.id = utils.generate_uuid()
        self.name = name
        self.parentId = parentId
        self.industyType = industyType

    def __repr__(self):
        return '<Industry %r>' % self.name if self.industyType == 1 else '<SegmentIndustry %r>' % self.name


#class SegmentIndustry(db.Model, BaseModel):
#    id = db.Column(db.String(36), primary_key=True, nullable=False)
#    name = db.Column(db.String(16), unique=True, nullable=False)
#    industry_id = db.Column(db.String(36), db.ForeignKey('industry.id'))
#
#    def __init__(self, name, industry_id):
#        self.id = utils.generate_uuid()
#        self.name = name
#        self.industry_id = industry_id
#
#    def __repr__(self):
#        return '<SegmentIndustry %r>' % self.name
#
