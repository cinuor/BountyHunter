# -*- coding: utf-8 -*-
import uuid, json
from .encrypt import *
from .response import *

def generate_uuid():
    id = uuid.uuid4()
    return str(id)

def get_data(request):
    data = getattr(request, 'data', None)
    if not data:
        return None
    return json.loads(request.data)

def capwords(words):
    result = list(words)
    result[0] = result[0].capitalize()
    return "".join(result)

def get_unique(id_list):
    print(id_list)
    if len(id_list) == 0:
        return tuple()
    result = set(id_list[0])
    for ids in id_list[1:]:
        if len(ids) == 0:
            continue
        result = result & set(ids)

    return tuple(result)
