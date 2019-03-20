# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from flask import Flask, jsonify, request, abort
from flask_restplus import Api, Resource, fields, reqparse
from sqlalchemy import create_engine
import os
import connexion
from sqlalchemy import or_, and_
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from config import db, ma
# from flask import make_response, abort
#from models import Person

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
    birthday = db.Column(db.DateTime)
    office = db.Column(db.String(32))
    employment = db.Column(db.DateTime)

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
                                'birthday': fields.DateTime(dt_format='iso8601', required=False, description='birthday', example="1991-07-21"),
                                'office': fields.String('Должность.', example="Инженер"),
                                'employment': fields.DateTime(dt_format='iso8601', required=False, description='employment', example="1991-07-21")
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
        try:
            new_people = api.payload
            db.session.add(Person(fio=new_people['fio'],
                              birthday=datetime.strptime(new_people['birthday'], '%Y-%m-%d'),
                              office=new_people['office'],
                              employment=datetime.strptime(new_people['employment'], '%Y-%m-%d')
                              )
                            )
            db.session.commit()
            return new_people, 201
        except ValueError:
            return 'Введенные данные неверные', 400
        # except TypeError:
        #     return 'Введенный тип данных неверный', 400
@api.route('/people/<id>')
class People1(Resource):
    def get(self,id):
        '''Выбрать человека по его ID'''
        person = Person.query.filter(Person.person_id == id).one_or_none()
        if person is not None:
            result = user_schema.dump(person)
            return result.data
        else:
            return {'Ненайден сотрудник с id №': id}, 404
    def delete(self, id):
        '''Удалить запись'''
        person = Person.query.filter(Person.person_id == id).one_or_none()
        if person is not None:
            db.session.delete(person)
            db.session.commit()
            return {'Удален сотрудник №': id}
        else:
            return {'Ненайден сотрудник с id №': id}, 404
    @api.expect(a_people)
    def post(self,id):
        '''Изменить запись'''
        new_people = api.payload
        try:
            person = Person.query.filter(Person.person_id == id).one_or_none()
            if person is not None:
                person.fio = new_people['fio']
                person.birthday = datetime.strptime(new_people['birthday'], '%d-%m-%Y')
                person.office = new_people['office']
                person.employment = datetime.strptime(new_people['employment'], '%d-%m-%Y')
                db.session.commit()
                return {'Изменен сотрудник №': id}
            else:
                return {'Ненайден сотрудник с id №': id}, 404
        except ValueError:
            return 'Введенные данные неверные', 400

@api.route('/people/filter')
@api.doc(params={'olderThan': 'Старше чем:',
                'yongerThan': 'Младше чем:',
                'exp1': 'Опыт работы больше чем:',
                'exp2': 'Опыт работы меньше чем:',
                'office': 'По должности:'})

class Item(Resource):
    def get(self):
        '''Фильтр по параметрам'''
        args = reqparse.RequestParser()
        olderThan = args.add_argument('olderThan').parse_args()['olderThan']
        yongerThan = args.add_argument('yongerThan').parse_args()['yongerThan']
        exp1 = args.add_argument('exp1').parse_args()['exp1']
        exp2 = args.add_argument('exp2').parse_args()['exp2']
        office = args.add_argument('office').parse_args()['office']
        try:
            query = Person.query
            if olderThan is not None:
                query = query.filter(and_(Person.birthday < (datetime.now() - timedelta(days=int(olderThan) * 365))))
            if yongerThan is not None:
                query = query.filter(and_(Person.birthday > (datetime.now() - timedelta(days=int(yongerThan) * 365))))
            if exp1 is not None:
                query = query.filter(and_(Person.employment < (datetime.now() - timedelta(days=int(exp1) * 365))))
            if exp2 is not None:
                query = query.filter(and_(Person.employment > (datetime.now() - timedelta(days=int(exp2) * 365))))
            if office is not None:
                query = query.filter(and_(Person.office == office))
        except OverflowError:
            return 'Ввдедите корректные значения', 400
        result = users_schema.dump(query).data
        if result == []:
            return 'Ничего не найденно', 404
        return result

if __name__ == '__main__':
    app.run()
