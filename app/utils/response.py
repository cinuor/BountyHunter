# -*- coding: utf-8 -*-

from flask import make_response, jsonify

__all__ = ['generate_resp']

def generate_resp(status_code, message=None, payload=None):

    if not message and not payload:
        resp = make_response()
    else:
        assert isinstance(payload, dict)
        body = dict(payload or ())
        if message:
            body['message'] = message
        resp = jsonify(body)

    resp.status_code = status_code
    return resp

