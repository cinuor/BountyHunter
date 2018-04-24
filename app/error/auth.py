# -*- coding: utf-8 -*-

from .base import BaseError

class UnauthorizedError(BaseError):
    status_code = 401

