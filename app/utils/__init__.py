# -*- coding: utf-8 -*-
import uuid, json
from .encrypt import *

def generate_uuid():
    return uuid.uuid4()

def get_post_data(request):
    data = getattr(request, 'data', None)
    if not data:
        return None
    return json.loads(request.data)

