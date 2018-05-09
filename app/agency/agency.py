# -*- coding: utf-8 -*-

import json
from flask import request, jsonify
from flask_restful import Resource, reqparse
from ..error import *
from ..models import Agency, Round, Investstage
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
        upperLimit = data.get('upperLimit')
        lowerLimit = data.get('lowerLimit')
        description = data.get('description', None)

        rounds = data.get('rounds')
        investstages = data.get('investstages')

        agency = Agency(name, fullname, nickname, website, capitalType, 
                capitalProperty, stageProperty, upperLimit, lowerLimit)

        self._insert_round(agency, rounds)
        self._insert_investstage(agency, investstages)

        Agency.add_entry(agency, True)
        return jsonify(agency.serialize())

    def _insert_round(self, agency, rounds):
        assert isinstance(agency, Agency)
        _rounds = Round.query.filter(Round.id.in_(rounds)).all()
        if len(_rounds) == 0:
            id_list = ", ".join(rounds)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.rounds.extend(_rounds)

    def _insert_investstage(self, agency, investstages):
        assert isinstance(agency, Agency)
        _investstages = Investstage.query.filter(Investstage.id.in_(investstages)).all()
        if len(_investstages) == 0:
            id_list = ", ".join(investstages)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.investstages.extend(_investstages)
