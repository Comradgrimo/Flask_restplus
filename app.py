# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields, reqparse
from sqlalchemy import create_engine
import os
import connexion
from sqlalchemy import or_, and_
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from config import db, ma
# from flask import make_response, abort
# from models import Person, PersonSchema

# conn = eng.connect()
# result = conn.execute('select * from person')
# print(result.first())



app = Flask(__name__)
api = Api(app, title='Сотрудники')


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(32))
    birthday = db.Column(db.String(32))
    office = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime,  default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    def __init__(self, fio, birthday, office):
        self.fio = fio
        self.birthday = birthday
        self.office = office


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('person_id', 'fio', 'birthday', 'office', 'timestamp' )


user_schema = UserSchema()
users_schema = UserSchema(many=True)


a_people = api.model('People', {'fio': fields.String('The language.'),
                                'birthday': fields.String('The birthday.'),
                                'office': fields.String('The office.')
                                  })
#
# PEOPLE = [
#     {"id": "1", "fio": "Иванов И.И", "birthday": "11.01.11", "office": "Инженер"},
#     {"id": "2", "fio": "Петров П.П", "birthday": "12.02.12", "office": "Уборщик"},
#     {"id": "3", "fio": "Сидоров С.С", "birthday": "13.03.13", "office": "Главбух"},
#  ]
# #PEOPLE = {'language' : 'aaaaa', 'id' : '1'}

@api.route('/people')
class People(Resource):
    def get(self):
        '''Показать все'''
        all_users = Person.query.order_by(Person.person_id).all()
        result = users_schema.dump(all_users)
        return result
    @api.expect(a_people)
    def put(self):
        '''Добавить человека'''
        new_people = api.payload
        db.session.add(Person(fio = new_people['fio'], birthday =new_people['birthday'], office =new_people['office']))
        db.session.commit()
        return new_people
#
@api.route('/people/<id>')
class People1(Resource):
    def get(self, id):
        '''Выбрать человека по его ID'''
        person = Person.query.filter(Person.person_id == id).one_or_none()
        if person is not None:
            result = users_schema.dump(person, id)
            return jsonify(result.data)
        else:
            return {'Ненайден сотрудник с id №': id}, 404
    def delete(self, id):
        '''Удалить запись'''
        person = Person.query.filter(Person.person_id == id).one_or_none()
        if person is not None:
            db.session.delete(person)
            db.session.commit()
            return {'deleted person id №': id}, 201
        else:
            return {'Ненайден сотрудник с id №': id}, 404
    @api.expect(a_people)
    def post(self,id):
        '''Изменить запись'''
        new_people = api.payload
        person = Person.query.filter(Person.person_id == id).one_or_none()
        if person is not None:
            person.fio = new_people['fio']
            person.birthday = new_people['birthday']
            person.office = new_people['office']
            db.session.commit()
            return {'update №': person.fio}, 201
        else:
            return {'Ненайден сотрудник с id №': id}, 404


@api.route('/people/filter')
@api.doc(params={'Person_id': 'An Person_id','office': 'An Office' })
class Item(Resource):
    def get(self):
        args = reqparse.RequestParser()
        Rq = args.add_argument('Person_id').parse_args()['Person_id']
        Rq1 = args.add_argument('office').parse_args()['office']
        args = args.parse_args()
        #Rq = args['arg']
        #Rq1 = args['arg1']
        person = Person.query.filter(and_(Person.person_id == Rq,Person.birthday == Rq1))
        result = users_schema.dump(person)
        return result
#api.add_resource(Item, '/people/office/Item')

if __name__ == '__main__':
    app.run(debug=True)


#
# def filter():
#     olderThan = request.args.get('olderThan', None)
#     yongerThan = request.args.get('yongerTnah', None)

