from flask import Blueprint
from flask_restplus import Api

from .beerroutes import api as ns1

api_bp = Blueprint('api', __name__)

api = Api(api_bp,
          title='Beer Collection API',
          version='1.0',
          description='All you need to know about beers for your application!'
          )

api.add_namespace(ns1)
