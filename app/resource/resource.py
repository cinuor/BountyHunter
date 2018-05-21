# -*- coding: utf-8 -*-

from flask import request, jsonify
from flask_restful import Resource, reqparse
from ..error import *
from ..models import resource
from ..models import Industry
from .. import utils

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True)

class EntriesResource(Resource):
    def get(self):
        args = parser.parse_args()
        resourceType = args['type']
        try:
            entry_class = getattr(resource, utils.capwords(resourceType))
        except KeyError:
            return BadRequestError(message='No Such Resource')

        entries = entry_class.query.all()
        return [entry.serialize() for entry in entries]

    def post(self):
        args = parser.parse_args()
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message='No Payload')
        try:
            resourceType = args['type']
            name = data['name']
            entry_class = getattr(resource, utils.capwords(resourceType))

            if resourceType.lower() == 'industry':
                parentId = data.get('parentId', None)
                industryType = data['industryType']
        except KeyError:
            raise BadRequestError(message='No Such Resource')

        if resourceType.lower() == 'industry':
            entry = entry_class(name, parentId, industryType)
        else:
            entry = entry_class(name)

        entry_class.add_entry(entry, True)
        return jsonify(entry.serialize())


class EntryResource(Resource):
    def get(self, id):
        try:
            args = parser.parse_args()
            resourceType = args['type']
            entry_class = getattr(resource, utils.capwords(resourceType))
        except KeyError:
            raise BadRequestError(message='No Such Resource')

        entry = entry_class.query.get(id);
        if not entry:
            raise NotFoundError(message='Resource %s Not Found' % id)
        
        return jsonify(entry.serialize())

    def put(self, id):
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message='No Payload')

        try:
            args = parser.parse_args()
            resourceType = args['type']
            name = data['name']
            entry_class = getattr(resource, utils.capwords(resourceType))
        except KeyError:
            raise BadRequestError(message='No Such Resource')
        
        entry = entry_class.query.get(id)
        if entry is None:
            raise NotFoundError(message='Resource %s Not Found' % id)
        entry.name = name
        entry.commit()
        return jsonify(entry.serialize())

    def delete(self, id):
        try:
            args = parser.parse_args()
            resourceType = args['type']
            entry_class = getattr(resource, utils.capwords(resourceType))
        except KeyError:
            raise BadRequestError(message='No Such Resource')

        entry = entry_class.query.get(id)
        if entry is None:
            raise NotFoundError(message='Resource %s Not Found' % id)
        entry_class.delete_entry(entry, True)
        resp = utils.generate_resp(200)
        return resp

