# -*- coding: utf-8 -*-

from flask import request, jsonify
from flask_restful import Resource
from ..error import *
from ..models import Agency
from .. import utils

class AgencyResource(Resource):
    def get(self, id):
        agency = Agency.query.filter_by(id=id).first()
        if not agency:
            raise NotFoundError(message='Resource %s Not Found' % id)
        return jsonify(agency.serialize())

    def delete(self, id):
        agency = Agency.query.filter_by(id=id).first()
        if agency is None:
            raise NotFoundError(message="Resource %s Not Found" % id)
        Agency.delete_entry(agency, True)
        resp = utils.generate_resp(200)
        return resp

    def put(self, id):
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message="No Payload")
        agency = Agency.query.filter_by(id=id).first()
        if not agency:
            raise NotFoundError(message='Resource %s Not Found' % id)
        for item in data.keys():
            setattr(agency, item, data[item])
        try:
            agency.commit()
        except SQLIntegrityError:
            raise BadRequestError(message="Duplicate Entry")
        resp = utils.generate_resp(200)
        return resp
         

class AgenciesResource(Resource):
    def get(self):
        agencies = Agency.query.all()
        if len(agencies) == 0:
            raise NotFoundError(message='No Entry Found')
        return jsonify([i.serialize() for i in agencies])

    def post(self):
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message="No Payload")

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
        #payload = dict(id=agency.id)
        resp = utils.generate_resp(200)
        return resp

