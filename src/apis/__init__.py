from flask_restplus import Api

from .beer_routes import ns as ns1
#from .namespace2 import api as ns2
# ...
#from .namespaceX import api as nsX

api = Api(
    title='Beer Collection API',
    version='1.0',
    description='All you need to know about beers for your application!',
    # All API metadatas
)

api.add_namespace(ns1)
# api.add_namespace(ns2)
# ...
# api.add_namespace(nsX)
