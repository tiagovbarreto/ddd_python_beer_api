
from flask_restplus import Namespace, Resource, fields

from src.app.commands import CreateBeerCommand, UpdateBeerCommand, DeleteBeerCommand
from src.app.queries import GetBeerByIDQuery, ListBeerQuery

api = Namespace('beers', description='Beers APIs')

model = api.model('Beer', {
    'id': fields.String(readonly=True, description='The beer unique identifier.'),
    'name': fields.String(required=True, description='The beer name.'),
    'kind': fields.String(required=True, description='The kind of the beer. Ex: Large'),
    'origin': fields.String(required=True, description='Country where the beer is originally produce.'),
    'alcohol': fields.String(required=True, description='The teor alcohol of the beer.'),
})


@api.route("")
class BeerList(Resource):

    @api.expect(model)
    @api.marshal_with(model)
    @api.respoapie(201, 'Success', model)
    def post(self):
        # cmd = CreateBeerCommand(api.payload)
        # res = cmd.execute()
        # return res, 201
        pass

    @api.marshal_list_with(model)
    def get(self):
        query = ListBeerQuery()
        records = [record.dict() for record in query.execute()]
        return records, 200

    @api.route('/<string:id>')
    @api.respoapie(404, 'Beer not found')
    @api.param('id', 'Beer identifier')
    class Beer(Resource):

        @api.marshal_with(model)
        def get(self, id):
            query = GetBeerByIDQuery(id=id)
            res = query.execute()
            return res

        @api.expect(model)
        @api.marshal_with(model)
        def put(self, id):
            cmd = UpdateBeerCommand(id=id, data=api.payload)
            res = cmd.execute()
            return res, 200

        @api.respoapie(204, 'Beer deleted')
        def delete(self, id):
            cmd = DeleteBeerCommand(id=id)
            cmd.execute()
            return '', 204
