import pytest
import uuid

from beer_api.domain.entities.beer import Beer
from beer_api.domain.valueobjects.refid import RefId
from beer_api.domain.valueobjects.beername import BeerName
from beer_api.domain.valueobjects.beerorigin import BeerOrigin


class TestBeer:

    def test_should_create(self):
        id = RefId.create(uuid.uuid4())
        name = BeerName.create("Boemia")
        origin = BeerOrigin.create("Brasil")
        instance = Beer(id, name, origin)

        assert isinstance(instance, Beer)
        assert instance.id == id
        assert instance.name == name
        assert instance.origin == origin

    def test_should_not_create_with_no_id(self):
        name = BeerName.create("Boemia")
        origin = BeerOrigin.create("Brasil")
        with pytest.raises(TypeError):
            Beer(name, origin)

    def test_should_not_create_with_no_name(self):
        id = RefId.create(uuid.uuid4())
        origin = BeerOrigin.create("Brasil")
        with pytest.raises(TypeError):
            Beer(id, origin)

    def test_should_not_create_with_no_origin(self):
        id = RefId.create(uuid.uuid4())
        name = BeerName.create("Boemia")
        with pytest.raises(TypeError):
            Beer(id, name)

    def test_should_not_create_with_none_id(self):
        id = None
        name = BeerName.create('Boemia')
        origin = BeerOrigin.create("Brasil")
        with pytest.raises(AssertionError):
            Beer(id, name, origin)

    def test_should_not_create_with_none_name(self):
        id = RefId.create(uuid.uuid4())
        name = None
        origin = BeerOrigin.create("Brasil")
        with pytest.raises(AssertionError):
            Beer(id, name, origin)

    def test_should_not_create_with_none_origin(self):
        id = RefId.create(uuid.uuid4())
        name = BeerName.create('Boemia')
        origin = None
        with pytest.raises(AssertionError):
            Beer(id, name, origin)
