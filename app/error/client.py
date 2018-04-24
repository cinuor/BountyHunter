# -*- coding: utf-8 -*-
from .base import BaseError


class BadRequestError(BaseError):
    status_code = 400

class NotFoundError(BaseError):
    status_code = 404
