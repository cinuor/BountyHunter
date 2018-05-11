# -*- coding: utf-8 -*-
from ..models import db
from .base import BaseModel
from .. import utils

agencyrounds = db.Table(
        'agencyrounds',
        db.Column('agency_id', db.String(36), db.ForeignKey('agency.id'), primary_key=True),
        db.Column('round_id', db.String(36), db.ForeignKey('round.id'), primary_key=True)
    )

agencyinveststages = db.Table(
        'agencyinveststages',
        db.Column('agency_id', db.String(36), db.ForeignKey('agency.id'), primary_key=True),
        db.Column('investstage_id', db.String(36), db.ForeignKey('investstage.id'), primary_key=True)
    )

agencyareas = db.Table(
        'agencyareas',
        db.Column('agency_id', db.String(36), db.ForeignKey('agency.id'), primary_key=True),
        db.Column('area_id', db.String(36), db.ForeignKey('area.id'), primary_key=True)
    )

agencycurrencys = db.Table(
        'agencycurrencys',
        db.Column('agency_id', db.String(36), db.ForeignKey('agency.id'), primary_key=True),
        db.Column('currency_id', db.String(36), db.ForeignKey('currency.id'), primary_key=True)
    )

agencytags = db.Table(
        'agencytags',
        db.Column('agency_id', db.String(36), db.ForeignKey('agency.id'), primary_key=True),
        db.Column('tag_id', db.String(36), db.ForeignKey('tag.id'), primary_key=True)
    )

agencyindustrys = db.Table(
        'agencyindustrys',
        db.Column('agency_id', db.String(36), db.ForeignKey('agency.id'), primary_key=True),
        db.Column('industry_id', db.String(36), db.ForeignKey('industry.id'), primary_key=True)
    )


class Agency(db.Model, BaseModel):
    __tablename__ = 'agency'
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
    description = db.Column(db.Text)

    rounds = db.relationship('Round', secondary=agencyrounds, lazy='dynamic', 
            backref=db.backref('agency', lazy='dynamic'))
    investstages = db.relationship('Investstage', secondary=agencyinveststages, lazy='dynamic',
            backref = db.backref('agency', lazy='dynamic'))
    areas = db.relationship('Area', secondary=agencyareas, lazy='dynamic',
            backref = db.backref('agency', lazy='dynamic'))
    currencys = db.relationship('Currency', secondary=agencycurrencys, lazy='dynamic',
            backref = db.backref('agency', lazy='dynamic'))
    tags = db.relationship('Tag', secondary=agencytags, lazy='dynamic',
            backref = db.backref('agency', lazy='dynamic'))
    industrys = db.relationship('Industry', secondary=agencyindustrys, lazy='dynamic',
            backref = db.backref('agency', lazy='dynamic'))

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

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'fullname': self.fullname,
            'nickname': self.nickname,
            'website': self.website,
            'capitalType': self.capitalType,
            'capitalProperty': self.capitalProperty,
            'stageProperty': self.stageProperty,
            'upperLimit': self.upperLimit,
            'lowerLimit': self.lowerLimit,
            'description': self.description,
            'rounds': [(_round.query.get(_round.id)).serialize() for _round in self.rounds],
            'investstages': [(_investstage.query.get(_investstage.id)).serialize() for _investstage in self.investstages],
            'areas': [(_area.query.get(_area.id)).serialize() for _area in self.areas],
            'currencys': [(_currency.query.get(_currency.id)).serialize() for _currency in self.currencys],
            'industrys': [(_industry.query.get(_industry.id)).serialize() for _industry in self.industrys],
            'tags': [(_tag.query.get(_tag.id)).serialize() for _tag in self.tags]
        }

    def serialize_simple(self):
        return {
            'id': self.id,
            'name': self.name,
            'fullname': self.fullname,
            'nickname': self.nickname,
            'website': self.website,
            'capitalType': self.capitalType,
            'capitalProperty': self.capitalProperty,
            'stageProperty': self.stageProperty,
            'upperLimit': self.upperLimit,
            'lowerLimit': self.lowerLimit,
            'description': self.description
        }
