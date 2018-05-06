# -*- coding: utf-8 -*-

from flask import request, jsonify
from flask_restful import Resource, reqparse
from ..error import *
from ..models import Round, InvestStage
from .. import utils

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True)

class EntriesResource(Resource):
    def get(self):
        args = parser.parse_args()
        resourceType = args['type']
        if resourceType == 'round':
            rounds = Round.query.all()
            return [_rounds.serialize() for _rounds in rounds]
        else:
            raise BadRequestError(message='No Such Resource')

    def post(self):
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message='No Payload')

        try:
            resourceType = data['type']
            name = data['name']
        except KeyError:
            raise BadRequestError(message='Not Enough Parameters')

        _round = Round(name)
        Round.add_entry(_round, True)
        return jsonify(_round.serialize())
        


class EntryResource(Resource):
    def get(self, id):
        args = parser.parse_args()
        print(args['type'])
        return id
