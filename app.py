# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from sqlalchemy import create_engine
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from config import db, ma
# from flask import make_response, abort
# from models import Person, PersonSchema

# conn = eng.connect()
# result = conn.execute('select * from person')
# print(result.first())



app = Flask(__name__)
api = Api(app)

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
        db.DateTime,  default=datetime.utcnow, onupdate=datetime.utcnow
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

PEOPLE = [
    {"id": "1", "fio": "Иванов И.И", "birthday": "11.01.11", "office": "Инженер"},
    {"id": "2", "fio": "Петров П.П", "birthday": "12.02.12", "office": "Уборщик"},
    {"id": "3", "fio": "Сидоров С.С", "birthday": "13.03.13", "office": "Главбух"},
 ]
#PEOPLE = {'language' : 'aaaaa', 'id' : '1'}

@api.route('/people')
class People(Resource):
    def get(self):
        all_users = Person.query.order_by(Person.person_id).all()
        result = users_schema.dump(all_users)
        return jsonify(result.data)
    @api.expect(a_people)
    def post(self):
        new_people = api.payload
        #new_people['person_id'] = (len(Person.query.all())) + 1
        #new_people['timestamp'] = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        db.session.add(Person(fio = 'bbbbb', birthday ='bbbbb', office ='bbbbbb'))
        db.session.commit()
        return new_people
#
@api.route('/people/<id>')
class People1(Resource):
    def get(self, id):
        person = Person.query.filter(Person.person_id == id).all()
        result = users_schema.dump(person, id)
        return jsonify(result.data)
#
#     def get(self, id):
#         res = [x for x in PEOPLE if x['id'] == id]
#         return {'result': res}, 201

if __name__ == '__main__':
    app.run(debug=True)