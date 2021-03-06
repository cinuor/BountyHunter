# -*- coding: utf-8 -*-

import json
import sqlalchemy
from functools import reduce
from flask import request, jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import text
from ..error import *
from sqlalchemy.exc import IntegrityError as SQLIntegrityError
from ..models import Agency, Round, InvestStage,\
        Area, Currency, Industry,Tag, db
from ..models import resource
from .. import utils

MUTIL_PROPERTY = ['areas', 'investStages', 
                'tags', 'industrys', 'rounds']

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
        global MUTIL_PROPERTY
        data = utils.get_data(request)
        if not data:
            raise BadRequestError(message="No Payload")
        agency = Agency.query.get(id)
        if not agency:
            raise NotFoundError(message='Resource %s Not Found' % id)
        for item in data.keys():
            if item in MUTIL_PROPERTY:
                ids = data[item]
                item = item.lower()[:-1]
                self.remove_all(item, id)
                self.insert_all(item, ids, id)
                continue
            setattr(agency, item, data[item])
        try:
            agency.commit()
        except SQLIntegrityError:
            raise BadRequestError(message="Duplicate Entry")
        resp = utils.generate_resp(200)
        return resp

    def _create_db_connection(self):
        global db
        return db.engine.connect()

    def remove_all(self, resourceType, agency_id):
        tablename = 'agency'+resourceType.lower()+'s'
        column = resourceType.lower()+'_id'

        connection = self._create_db_connection()
        sql = "DELETE FROM {0} WHERE agency_id={1}".format(tablename, agency_id)
        try:
            connection.execute(sql)
        except:
            raise

    def insert_all(self, resourceType, ids, agency_id):
        tablename = 'agency'+resourceType.lower()+'s'
        column = resourceType.lower()+'_id'

        connection = self._create_db_connection()

        for property_id in ids:
            sql = "INSERT INTO {0} (agency_id, {1}) VALUES ({2},{3})"\
                    .format(tablename, column, agency_id, property_id)
            print(sql)
            try:
                connection.execute(sql)
            except:
                raise
         

class AgenciesResource(Resource):

#    parameters = ['industry', 'segindustry', 'capitalType', 
#            'capitalProperty', 'stageProperty', 'investStage',
#            'round', 'currency', 'area', 'investCount', 'tag']
    parameters = [
        ('name',            False),
        ('industry',        False),
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

        name = args['name'][0] if args['name'] else None
        capitaltype = tuple(args['capitalType']) if args['capitalType'] else None
        capitalproperty = tuple(args['capitalProperty']) if args['capitalProperty'] else None
        stageproperty = tuple(args['stageProperty']) if args['stageProperty'] else None
        currency = tuple(args['currency']) if args['currency'] else None
        investcount = int(args['investCount'][0]) if args['investCount'] else None


        connection = self._create_db_connection()
        trans = self._create_db_trans(connection)
        try:
            industry_agencies = self.get_agencies_from_entries(connection, 
                    'agencyindustrys', 'industry_id', args['industry'])
            investstage_agencies = self.get_agencies_from_entries(connection,
                    'agencyinveststages', 'investstage_id', args['investStage'])
            round_agencies = self.get_agencies_from_entries(connection, 
                    'agencyrounds', 'round_id', args['round'])
            #currency_agencies = self.get_agencies_from_entries(connection, 
            #        'agencycurrencys', 'currency_id', args['currency'])
            area_agencies = self.get_agencies_from_entries(connection, 
                    'agencyareas', 'area_id', args['area'])
            tag_agencies = self.get_agencies_from_entries(connection,
                    'agencytags', 'tag_id', args['tag'])

            trans.commit()
        except:
            trans.rollback()
            raise ServerError(message="Database Error")
        
        print(industry_agencies)
        print(investstage_agencies)
        print(round_agencies)
        print(area_agencies)
        print(tag_agencies)


        agency_ids = list()
        agency_ids.append(industry_agencies)
        agency_ids.append(investstage_agencies)
        agency_ids.append(round_agencies)
        #agency_ids.append(currency_agencies)
        agency_ids.append(area_agencies)
        agency_ids.append(tag_agencies)

        result = utils.get_unique(agency_ids)
        print(result)
        query = Agency.query
        
        if name:
            query = query.filter(Agency.name.like("%"+name+"%"))
        if capitaltype:
            query = query.filter(Agency.capitalType.in_(capitaltype))
        if capitalproperty:
            query = query.filter(Agency.capitalProperty.in_(capitalProperty))
        if stageproperty:
            query = query.filter(Agency.stageProperty.in_(stageproperty))
        if currency:
            query = query.filter(Agency.currency.in_(currency))
        if investcount:
            query = query.filter(Agency.lowerLimit <= investcount)
            query = query.filter(Agency.upperLimit >= investcount)
        if len(result) > 0:
            query = query.filter(Agency.id.in_(result))

        agencies = query.all()

        #def suit(investcount):
        #    return lambda x: x.lowerLimit <= investcount \
        #            and x.upperLimit >= investcount
        
        #agencies = filter(suit(investcount), agencies)

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
            currency = data['currency']
            upperLimit = data['upperLimit']
            lowerLimit = data['lowerLimit']
        except KeyError:
            raise BadRequestError(message="No Enough Parameter")

        fullname = data.get('fullname', None)
        nickname = data.get('nickname', None)
        website = data.get('website', None)
        description = data.get('description', None)

        rounds = data.get('rounds', None)
        investstages = data.get('investStages', None)
        areas = data.get('areas', None)
        industrys = data.get('industrys', None)
        tags = data.get('tags', None)

        try:
            agency = Agency(name, fullname, nickname, website, 
                    capitalType, capitalProperty, stageProperty, 
                    currency, upperLimit, lowerLimit, description)
            self._insert_round(agency, rounds)
            self._insert_investstage(agency, investstages)
            self._insert_area(agency, areas)
            #self._insert_currency(agency, currencys)
            self._insert_industry(agency, industrys)
            self._insert_tag(agency, tags)
            Agency.add_entry(agency, True)
        except SQLIntegrityError:
            raise BadRequestError(message='Duplicate Entry')

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
        _investstages = InvestStage.query.filter(InvestStage.id.in_(investstages)).all()
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

#   def _insert_currency(self, agency, currencys):
#       if not currencys:
#           return
#       assert isinstance(agency, Agency)
#       _currencys = Currency.query.filter(Currency.id.in_(currencys)).all()
#       if len(_currencys) == 0:
#           id_list = ", ".join(areas)
#           raise NotFoundError(message="Resource %s Not Found" % id_list)
#       agency.currencys.extend(_currencys)

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
        if not entries:
            return []
        sql = "SELECT agency_id FROM {0} WHERE {1} in :ids".format(table, column)
        rows = connection.execute(text(sql), ids = tuple(entries)).fetchall()
        return [row[0] for row in rows]

class AgencyProperty(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str, required=True)

    def put(self, id):
        """
        body:
        {
            'type': 'round',
            'entries': [
                'round_id_1',
                'round_id_2',
                'round_id_3'
            ]
        }
        """

        data_list = utils.get_data(request)
        if not data_list:
            raise BadRequestError(message='No Payload')
        
        for data in data_list:
            try:
                resourceType = data['type']
                id_list = data['entries']
            except KeyError:
                raise BadRequestError(message='Not Enough Parameter')

            self.remove_all(resourceType, id)

            if len(id_list) == 0:
                continue

            agency = Agency.query.get(id)
            if not agency:
                raise NotFoundError(message="Agency %s Not Found" % id)


            try:
                entry_class = getattr(resource, utils.capwords(resourceType))
                entries = entry_class.query.filter(entry_class.id.in_(id_list)).all()
                if len(id_list) != len(entries):
                    raise BadRequestError(message='No Such Resource')
        
                resourceType = resourceType.lower() + 's'

                agency_entries = getattr(agency, resourceType)
                agency_entries.extend(entries)
                db.session.commit()

            except KeyError:
                raise BadRequestError(message='No Such Resource')
            except:
                raise
	
        resp = utils.generate_resp(200)
        return resp

    def remove_all(self, resourceType, agency_id):
        tablename = 'agency'+resourceType.lower()+'s'
        column = resourceType.lower()+'_id'

        connection = self._create_db_connection()
        sql = "DELETE FROM {0} WHERE agency_id={1}".format(tablename, agency_id)
        try:
            connection.execute(sql)
        except:
            raise

    def delete(self, id, resourceId=None):

        if not resourceId:
            raise BadRequestError(message='Not Enough Parameter')

        args = self.parser.parse_args()
        resourceType = args['type']

        tablename = 'agency'+resourceType.lower()+'s'
        column = resourceType.lower()+'_id'

        connection = self._create_db_connection()
        sql = "DELETE FROM {0} WHERE agency_id={1} AND {2}={3}".format(tablename, id, column, resourceId)
        print(sql)
        try:
            connection.execute(sql)
        except:
            raise
        resp = utils.generate_resp(200)
        return resp

    def _create_db_connection(self):
        global db
        return db.engine.connect()

    def _create_db_trans(self, connection):
        return connection.begin()
        
