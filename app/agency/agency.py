# -*- coding: utf-8 -*-

from flask import request, make_response, redirect
from flask_restful import Resource
from ..error import *
from ..models import Agency
from .. import utils

class AgencyResource(Resource):
    def get(self, id):
        agency = Agency.query.filter_by(id=id).first()
        print(agency)
        return "ok"


class AgenciesResource(Resource):
    def get(self):
        agencies = Agency.query.all()
        print(agencies)
        return agencies

    def post(self):
        data = utils.get_post_data(request)
        if not data:
            raise BadRequestError(message="No Payload")

        #id = utils.generate_uuid()
        name = data.get('name')
        fullname = data.get('fullname', None)
        nickname = data.get('nickname', None)
        website = data.get('website', None)
        capitalType = data.get('capitalType')
        capitalProperty = data.get('capitalProperty')
        stageProperty = data.get('stageProperty')
        upperLimit = int(data.get('upperLimit'))
        lowerLimit = int(data.get('lowerLimit'))

        agency = Agency(name, fullname, nickname, website, capitalType, 
                capitalProperty, stageProperty, upperLimit, lowerLimit)

        Agency.add_entry(agency, True)
        return "ok"
