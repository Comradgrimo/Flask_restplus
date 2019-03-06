# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from config import db, ma
from flask import make_response, abort
from models import Person, PersonSchema

app = Flask(__name__)
api = Api(app)

a_people = api.model('People', {'id': fields.String('The id.'),
                                'fio': fields.String('The language.'),
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
        return PEOPLE, 201
    @api.expect(a_people)
    def post(self):
        new_people = api.payload
        new_people['id'] = len(PEOPLE)+1
        PEOPLE.append(new_people)
        return {'result': 'people added'}, 201

@api.route('/people/<id>')
class People1(Resource):
    def put(self, id):
        new_people = api.payload
        res = [x for x in PEOPLE if x['id'] == id]
        res[0].update(new_people)
        return {'result': 'people update'}, 201

    def get(self, id):
        res = [x for x in PEOPLE if x['id'] == id]
        return {'result': res}, 201

if __name__ == '__main__':
    app.run(debug=True)