# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

agencybp = Blueprint('agency', __name__)

from .agency import AgencyProperty, AgenciesResource, AgencyResource

agency_api = Api(agencybp)
agency_api.add_resource(AgenciesResource, '/agencies')
agency_api.add_resource(AgencyResource, '/agencies/<string:id>')
agency_api.add_resource(AgencyProperty, 
        '/agencies/<string:id>/change', 
        '/agencies/<string:id>/delete/<string:resourceId>')
