import os
from flask import request
from flask_restplus import Namespace, Resource, fields

from app.main.application.commands.beercreate import CreateBeerCommand
from app.main.domain.usecases.beercreatedto import CreateBeerDTO
from app.main.domain.usecases.createbeer import CreateBeerUseCase
from app.main.application.commands.beercreate import CreateBeerCommand
from app.main.infrastructure.database.sqlite.beerrepository import SQLiteBeerRepository
from app.main.infrastructure.database.slqalchemy.beerrepository import SQLACBeerRepository

api = Namespace('beers', description='Beers APIs')

model = api.model('Beer', {
    'id': fields.String(readonly=True, description='The beer unique identifier.'),
    'name': fields.String(required=True, description='The beer name.'),
})


@api.route("")
class BeerList(Resource):

    @api.expect(model)
    @api.marshal_with(model)
    @api.response(201, 'Success', model)
    def post(self):

        # TODO move this initialization to a application config function
        # that will be called by the initialization function of the application.
        beer_repository = SQLACBeerRepository()
        # beer_repository = SQLiteBeerRepository(
        #     os.getenv("DATABASE_NAME", "database.db"))
        create_beer_usecase = CreateBeerUseCase(beer_repository)
        create_beer_command = CreateBeerCommand(create_beer_usecase)

        dto = CreateBeerDTO(**request.json)
        res = create_beer_command.execute(dto)
        return res, 201

    # @api.marshal_list_with(model)
    # def get(self):
    #     query = ListBeerQuery()
    #     records = [record.dict() for record in query.execute()]
    #     return records, 200

    # @api.route('/<string:id>')
    # @api.response(404, 'Beer not found')
    # @api.param('id', 'Beer identifier')
    # class Beer(Resource):

    #     @api.marshal_with(model)
    #     def get(self, id):
    #         query = GetBeerByIDQuery(id=id)
    #         res = query.execute()
    #         return res

    #     @api.expect(model)
    #     @api.marshal_with(model)
    #     def put(self, id):
    #         cmd = UpdateBeerCommand(id=id, data=api.payload)
    #         res = cmd.execute()
    #         return res, 200

    #     @api.response(204, 'Beer deleted')
    #     def delete(self, id):
    #         cmd = DeleteBeerCommand(id=id)
    #         cmd.execute()
    #         return '', 204
