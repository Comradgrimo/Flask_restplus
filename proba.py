from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Define parser and request args



class Item(Resource):
   def get(self):
       parser = reqparse.RequestParser()
       parser.add_argument('class', type=list)
       args = parser.parse_args()
       classes = args['class']  # List ['A', 'B']
       return {'summary': classes[0]}


api.add_resource(Item, '/item')