# -*- coding: utf-8 -*-

import json
from flask import request, jsonify
from flask_restful import Resource, reqparse
from ..error import *
from ..models import Agency, Round
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

    parameters = ['industry', 'segindustry', 'capitalType', 
            'capitalProperty', 'stageProperty', 'investStage',
            'round', 'currency', 'area', 'investCount', 'tag']
    parser = reqparse.RequestParser()
    for para in parameters:
        parser.add_argument(para, type=str, action='append')
    #parser.add_argument('industry', type=str, action='append')
    #parser.add_argument('segindustry', type=str, action='append')
    #parser.add_argument('capitalType', type=str, action='append')
    #parser.add_argument('capitalProperty', type=str, action='append')
    #parser.add_argument('stageProperty', type=str, action='append')
    #parser.add_argument('investStage', type=str, action='append')
    #parser.add_argument('round', type=str, action='append')
    #parser.add_argument('currency', type=str, action='append')
    #parser.add_argument('area', type=str, action='append')
    #parser.add_argument('investCount', type=str, action='append')
    #parser.add_argument('tag', type=str, action='append')

    def get(self):
        args = self.parser.parse_args()
        print(args)
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
        description = data.get('description', None)

        rounds = data.get('rounds')

        agency = Agency(name, fullname, nickname, website, capitalType, 
                capitalProperty, stageProperty, upperLimit, lowerLimit)

        self._insert_round(agency, rounds)

        Agency.add_entry(agency, True)
        return jsonify(agency.serialize())

    def _insert_round(self, agency, rounds):
        assert isinstance(agency, Agency)
        _rounds = Round.query.filter(Round.id.in_(rounds)).all()
        agency.rounds.extend(_rounds)
