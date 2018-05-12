# -*- coding: utf-8 -*-

import json
from flask import request, jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import text
from ..error import *
from ..models import Agency, Round, Investstage,\
        Area, Currency, Industry,Tag, db
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

#    parameters = ['industry', 'segindustry', 'capitalType', 
#            'capitalProperty', 'stageProperty', 'investStage',
#            'round', 'currency', 'area', 'investCount', 'tag']
    parameters = [
        ('industry',        False),
        ('segindustry',     False),
        ('capitalType',     False),
        ('capitalProperty', False),
        ('stageProperty',   False),
        ('investStage',     False),
        ('round',           False),
        ('currency',        False),
        ('area',            False),
        ('investCount',     False),
        ('tag',             False)
    ]
    parser = reqparse.RequestParser()
    for para in parameters:
        parser.add_argument(para[0], type=str, action='append', required=para[1])

    def get(self):
        args = self.parser.parse_args()
        print(args)
        connection = self._create_db_connection()
        trans = self._create_db_trans(connection)
        try:
            industry_agencies = self.get_agencies_from_entries(connection, 
                    'agencyindustrys', 'industry_id', args['industry'])

            trans.commit()
        except:
            trans.rollback()
            raise ServerError(message="Database Error")

        print(industry_agencies)
        agencies = Agency.query.all()
        return jsonify([i.serialize_simple() for i in agencies])

    def post(self):
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message="No Payload")

        try:
            name = data['name']
            capitalType = data['capitalType']
            capitalProperty = data['capitalProperty']
            stageProperty = data['stageProperty']
            upperLimit = data['upperLimit']
            lowerLimit = data['lowerLimit']
        except KeyError:
            raise BadRequestError(message="No Enough Parameter")

        fullname = data.get('fullname', None)
        nickname = data.get('nickname', None)
        website = data.get('website', None)
        description = data.get('description', None)

        rounds = data.get('rounds', None)
        investstages = data.get('investstages', None)
        areas = data.get('areas', None)
        currencys = data.get('currencys', None)
        industrys = data.get('industrys', None)
        tags = data.get('tags', None)

        agency = Agency(name, fullname, nickname, website, capitalType, 
                capitalProperty, stageProperty, upperLimit, lowerLimit)

        self._insert_round(agency, rounds)
        self._insert_investstage(agency, investstages)
        self._insert_area(agency, areas)
        self._insert_currency(agency, currencys)
        self._insert_industry(agency, industrys)
        self._insert_tag(agency, tags)


        Agency.add_entry(agency, True)
        return jsonify(agency.serialize())

    def _insert_round(self, agency, rounds):
        if not rounds:
            return
        assert isinstance(agency, Agency)
        _rounds = Round.query.filter(Round.id.in_(rounds)).all()
        if len(_rounds) == 0:
            id_list = ", ".join(rounds)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.rounds.extend(_rounds)

    def _insert_investstage(self, agency, investstages):
        if not investstages:
            return
        assert isinstance(agency, Agency)
        _investstages = Investstage.query.filter(Investstage.id.in_(investstages)).all()
        if len(_investstages) == 0:
            id_list = ", ".join(investstages)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.investstages.extend(_investstages)

    def _insert_area(self, agency, areas):
        if not areas:
            return
        assert isinstance(agency, Agency)
        _areas = Area.query.filter(Area.id.in_(areas)).all()
        if len(_areas) == 0:
            id_list = ", ".join(areas)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.areas.extend(_areas)

    def _insert_currency(self, agency, currencys):
        if not currencys:
            return
        assert isinstance(agency, Agency)
        _currencys = Currency.query.filter(Currency.id.in_(currencys)).all()
        if len(_currencys) == 0:
            id_list = ", ".join(areas)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.currencys.extend(_currencys)

    def _insert_industry(self, agency, industrys):
        if not industrys:
            return
        assert isinstance(agency, Agency)
        _industrys = Industry.query.filter(Industry.id.in_(industrys)).all()
        if len(_industrys) == 0:
            id_list = ", ".join(industrys)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.industrys.extend(_industrys)

    def _insert_tag(self, agency, tags):
        if not tags:
            return
        assert isinstance(agency, Agency)
        _tags = Tag.query.filter(Tag.id.in_(tags)).all()
        if len(_tags) == 0:
            id_list = ", ".join(tags)
            raise NotFoundError(message="Resource %s Not Found" % id_list)
        agency.tags.extend(_tags)

    def _create_db_connection(self):
        global db
        return db.engine.connect()

    def _create_db_trans(self, connection):
        return connection.begin()

    def get_agencies_from_entries(self, connection, table, column, entries):
        sql = "SELECT agency_id FROM {0} WHERE {1} in :ids".format(table, column)
        rows = connection.execute(text(sql), ids = tuple(entries)).fetchall()
        return [row[0] for row in rows]
