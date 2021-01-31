import json
import pathlib

import pytest
from jsonschema import validate, RefResolver

from app.app import app
from app.models import Beer


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
    data = {
        'name': 'Budweiser',
        'kind': 'Larger',
        'origin': 'USA',
        'alcohol': '5'
    }
    response = client.post(
        '/beers',
        data=json.dumps(
            data
        ),
        content_type='application/json',
    )

    validate_payload(response.json, 'Beer.json')
