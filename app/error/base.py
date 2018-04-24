# -*- coding: utf-8 -*-

class BaseError(Exception):
    status_code = 200

    def __init__(self, message=None, status_code=None, payload=None):
        super(BaseException, self).__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        if self.message is not None:
            rv["message"] = self.message
        return rv
