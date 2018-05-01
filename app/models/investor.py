# -*- coding: utf-8 -*-

from ..models import db
from .base import BaseModel
from .. import utils


class Investor(db.Model, BaseModel):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db)
    englishName = db.Column(db.String(20))
    workEmail = db.Column(db.String(50), nullable=False)
    personEmail = db.Column(db.String(50))
    phonenumberOne = db.Column(db.String(16), nullable=False)
    phonenumberTwo = db.Column(db.String(16))
    phonenumberThree = db.Column(db.String(16))
    province = db.Column(db.String(8))
    city = db.Column(db.String(10))
    area = db.Column(db.String(20))
    address = db.Column(db.String(100))
    description = db.Column(db.Text)
    note = db.Column(db.Text)
