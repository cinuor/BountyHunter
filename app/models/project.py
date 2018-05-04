# -*- coding: utf-8 -*-

from ..models import db
from .base import BaseModel
from .. import utils

class Project(db.model, BaseModel):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), nullable=True, unique=True)
