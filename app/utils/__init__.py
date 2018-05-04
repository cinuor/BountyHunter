# -*- coding: utf-8 -*-
import uuid, json
from .encrypt import *

def generate_uuid():
    id = uuid.uuid4()
    return str(id)

def get_post_data(request):
    data = getattr(request, 'data', None)
    if not data:
        return None
    return json.loads(request.data)

