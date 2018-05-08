# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

resourcebp = Blueprint('resource', __name__)

from .resource import *

resource_api = Api(resourcebp)
resource_api.add_resource(EntriesResource, '/resource')
resource_api.add_resource(EntryResource, '/resource/<string:id>')
