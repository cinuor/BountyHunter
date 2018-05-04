# -*- coding: utf-8 -*-

import enum
from ..models import db
from .base import BaseModel
from .. import utils

class SexEnum(enum.Enum):
    male = 1
    female = 2
    other = 3

class JobStatusEnum(enum.Enum):
    onthejob = 1
    offthejob = 2
    other = 3

class Investor(db.Model, BaseModel):
    __tablename__ = 'investor'
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.Enum(SexEnum))
    englishName = db.Column(db.String(20))
    workEmail = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50))
    personEmail = db.Column(db.String(50))
    phonenumberOne = db.Column(db.String(16), nullable=False)
    phonenumberTwo = db.Column(db.String(16))
    phonenumberThree = db.Column(db.String(16))
    wechat = db.Column(db.String(15))
    qq = db.Column(db.String(15))
    province = db.Column(db.String(8))
    city = db.Column(db.String(10))
    area = db.Column(db.String(20))
    address = db.Column(db.String(100))
    jobStatus = db.Column(db.Enum(JobStatusEnum))
    preference = db.Column(db.Text)
    description = db.Column(db.Text)
    note = db.Column(db.Text)

    def __init__(self, name, sex, englishName, workEmail, personEmail, department, 
            phonenumberOne, phonenumberTwo, phonenumberThree, wechat, qq, 
            province, city, area, address, jobStatus, preference, description, note):
        
        self.id = utils.generate_uuid()
        self.name = name
        self.sex = sex
        self.englishName = englishName
        self.workEmail = workEmail
        self.personEmail = personEmail
        self.department = department
        self.phonenumberOne = phonenumberOne
        self.phonenumberTwo = phonenumberTwo
        self.phonenumberThree = phonenumberThree
        self.wechat = wechat
        self.qq = qq
        self.province = province
        self.city = city
        self.area = area
        self.address = address
        self.jobStatus = jobStatus
        self.preference = preference
        self.description = description
        self.note = note

    def __repr__(self):
        return '<Investor %r>' % self.name
    
