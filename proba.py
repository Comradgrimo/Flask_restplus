# from flask import Flask
# from flask_restful import Api, Resource, reqparse
#
# app = Flask(__name__)
# api = Api(app)
#
# # Define parser and request args
#
#
#
# class Item(Resource):
#    def get(self):
#        parser = reqparse.RequestParser()
#        parser.add_argument('class', type=list)
#        args = parser.parse_args()
#        classes = args['class']  # List ['A', 'B']
#        return {'summary': classes[0]}
#
#
# api.add_resource(Item, '/item')
from datetime import datetime, date
a = datetime.strftime(datetime.now(), '%Y-%m-%d')
c = datetime.strptime('2019-03-11', '%Y-%m-%d')
v = date.today()
print(type(a))
print(a)
print(c)
