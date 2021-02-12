from flask_restplus import Api
from .beerroutes import api as ns1

api = Api(
    title='Beer Collection API',
    version='1.0',
    description='All you need to know about beers for your application!'
)

api.add_namespace(ns1)
