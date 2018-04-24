# -*- coding: utf-8 -*-

from ..models import db

class BaseModel(object):

    @staticmethod
    def add_entry(entry, autocommit=False):
        db.session.add(entry)
        if autocommit:
            db.session.commit()

    @staticmethod
    def delete_entry(entry, autocommit=False):
        db.session.delete(entry)
        if autocommit:
            db.session.commit()

    def commit(self):
        db.session.commit()

