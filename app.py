# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
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
from models import Person

# conn = eng.connect()
# result = conn.execute('select * from person')
# print(result.first())



app = Flask(__name__)
api = Api(app, title='Сотрудники')


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# class Person(db.Model):
#     __tablename__ = 'person'
#     person_id = db.Column(db.Integer, primary_key=True)
#     fio = db.Column(db.String(32))
#     birthday = db.Column(db.String(32))
#     office = db.Column(db.String(32))
#     timestamp = db.Column(
#         db.DateTime,  default=datetime.utcnow(), onupdate=datetime.utcnow()
#     )

def __init__(self, fio, birthday, office, employment):
    self.fio = fio
    self.birthday = birthday
    self.office = office
    self.employment = employment

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('person_id', 'fio', 'birthday', 'office', 'employment' )


user_schema = UserSchema()
users_schema = UserSchema(many=True)


a_people = api.model('People', {'fio': fields.String('Имя фамилия отчество.', example="Иванов И.И"),
                                'birthday': fields.DateTime(dt_format='iso8601', required=False, description='birthday', example="DD-MM-YYYY"),
                                'office': fields.String('Должность.', example="Инженер"),
                                'employment': fields.DateTime('Дата приема на работу.',description='birthday', example="DD-MM-YYYY")
                                  })

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
        db.session.add(Person(fio = new_people['fio'], birthday =datetime.strptime(new_people['birthday'], '%d-%m-%Y'), office =new_people['office'], employment=new_people['employment'] ))
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
            person.employment = new_people['employment']
            db.session.commit()
            return {'update №': person.fio}, 201
        else:
            return {'Ненайден сотрудник с id №': id}, 404


@api.route('/people/filter')
@api.doc(params={'olderThan': 'Старше чем:','yongerThan': 'Младше чем:' })
class Item(Resource):
    def get(self):
        args = reqparse.RequestParser()
        olderThan = args.add_argument('olderThan').parse_args()['olderThan']
        yongerThan = args.add_argument('yongerThan').parse_args()['yongerThan']
        args = args.parse_args()
        #Rq = args['arg']
        #Rq1 = args['arg1']
        if olderThan is not None and yongerThan is not None:
            person = Person.query.filter(and_(Person.birthday < (datetime.now()-timedelta(days=int(olderThan) * 365)),
                                     Person.birthday > (datetime.now()-timedelta(days=int(yongerThan) * 365))
                                     ))
            result = users_schema.dump(person).data
            return result

        if olderThan == None:
                person = Person.query.filter(Person.birthday > (datetime.now() - timedelta(days=int(yongerThan) * 365)))
                result = users_schema.dump(person).data
                return result

        if yongerThan == None:
                person = Person.query.filter(Person.birthday < (datetime.now() - timedelta(days=int(olderThan) * 365)))
                result = users_schema.dump(person).data
                return result

        # if Rq1 == '>':
        #     person = Person.query.filter(Person.birthday > (datetime.now()-timedelta(days=int(Rq) * 365))).all()
        #     result = users_schema.dump(person).data
        #     return result
        # if Rq1 == '<':
        #     person = Person.query.filter(Person.birthday < (datetime.now()-timedelta(days=int(Rq) * 365))).all()
        #     result = users_schema.dump(person).data
        #     return result
        #for i in range(4): mn = result[i].get('birthday')
        #return person
        #if round((datetime.now() - Person.birthday).days / 365) < Rq:
           # person = Person.query.filter(and_(Person.person_id == Rq, Person.birthday < date.today() ))
            #result = users_schema.dump(person)
             #return {'КАЕФ': id}
#api.add_resource(Item, '/people/office/Item')
#str(datetime.timedelta(seconds=500000))

if __name__ == '__main__':
    app.run(debug=True)


#
# def filter():
#     olderThan = request.args.get('olderThan', None)
#     yongerThan = request.args.get('yongerTnah', None)

