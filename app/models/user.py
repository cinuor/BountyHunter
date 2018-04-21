# -*- coding: utf-8 -*-
from BountyHunter.app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column()
