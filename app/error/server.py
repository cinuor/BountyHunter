# -*- coding: utf-8 -*-

from .base import BaseError

class ServerError(BaseError):
    status_code = 500
