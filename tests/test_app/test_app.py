import json
import pathlib

import pytest
from jsonschema import validate, RefResolver

from src.app import app
from src.domain.entities.beer import Beer


def makePostBeer(client):
     return client.post('/beers', data=json.dumps(data),content_type='application/json',)

data = {
   'name': 'Budweiser',
   'kind': 'Larger',
   'origin': 'United States of America',
   'alcohol': '5.0'
}

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def validate_payload(payload, schema_name):
    """
    Validate payload with selected schema
    """
    schemas_dir = str(
        f'{pathlib.Path(__file__).parent.absolute()}/schemas'
    )
    schema = json.loads(pathlib.Path(
        f'{schemas_dir}/{schema_name}').read_text())
    validate(
        payload,
        schema,
        resolver=RefResolver(
            'file://' +
            str(pathlib.Path(f'{schemas_dir}/{schema_name}').absolute()),
            schema  # it's used to resolve file: inside schemas correctly
        )
    )


def test_create_beer(client):
    """
    GIVEN request data for new beer
    WHEN endpoint /beers is called
    THEN it should return beer in json format matching schema
    """

    response = makePostBeer(client) 
    validate_payload(response.json, 'Beer.json')


# def test_get_beer_by_id(client):
#     """
#     GIVEN ID of beer stored in the database
#     WHEN endpoint /beer/<id-of-beer>/ is called
#     THEN it should return beer in json format matching schema
#     """

#     response = client.get(
#         f'/beers/{treta.id}',
#         content_type='application/json',
#     )

#     validate_payload(response.json, 'Beer.json')


# def test_list_beers(client):
#     """
#     GIVEN beers stored in the database
#     WHEN endpoint /beers is called
#     THEN it should return list of beer in json format matching schema
#     """
#     Beer(
#         name='Budweiser',
#         kind='Larger',
#         origin='USA',
#         alcohol='5'
#     ).save()
#     response = client.get(
#         '/beers',
#         content_type='application/json',
#     )

#     validate_payload(response.json, 'BeerList.json')
