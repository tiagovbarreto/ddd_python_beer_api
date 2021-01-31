from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields

from src.commands import CreateBeerCommand
from src.queries import GetBeerByIDQuery, ListBeerQuery

app = Flask(__name__)

api = Api(app, version="1.0",
          title="Beers Collection",
          description="All you need about beers for your application")

ns = api.namespace('beers', description='Beers APIs')

model = api.model('Beer', {
    'id': fields.String(readonly=True, description='The beer unique identifier.'),
    'name': fields.String(required=True, description='The beer name.'),
    'kind': fields.String(required=True, description='The kind of the beer. Ex: Large'),
    'origin': fields.String(required=True, description='Country where the beer is originally produce.'),
    'alcohol': fields.String(required=True, description='The teor alcohol of the beer.'),
})


@ ns.route("")
class BeerList(Resource):

    @ns.expect(model)
    @ns.marshal_with(model)
    @ns.response(201, 'Success', model)
    def post(self):
        cmd = CreateBeerCommand(**request.json)
        res = cmd.execute()
        return res, 201

    @ns.marshal_list_with(model)
    def get(self):
        query = ListBeerQuery()
        records = [record.dict() for record in query.execute()]
        return records, 200


@ns.route('/<string:id>')
@ns.response(404, 'Beer not found')
@ns.param('id', 'The task identifier')
class Beer(Resource):
    @ns.marshal_with(model)
    def get(self, id):
        query = GetBeerByIDQuery(id=id)
        res = query.execute()
        return res


if __name__ == '__main__':
    app.run()
