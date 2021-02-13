import pytest
import uuid

from app.main.domain.entities.beer import Beer
from app.main.domain.valueobjects.refid import RefId
from app.main.domain.valueobjects.beername import BeerName


class TestBeer:

    def test_should_create(self):
        id = RefId.create(uuid.uuid4())
        name = BeerName.create("Boemia")
        instance = Beer(id, name)

        assert isinstance(instance, Beer)
        assert instance.id == id
        assert instance.name == name

    def test_should_not_create_with_no_id(self):
        name = BeerName.create("Boemia")
        with pytest.raises(TypeError):
            Beer(name)

    def test_should_not_create_with_no_name(self):
        id = RefId.create(uuid.uuid4())
        with pytest.raises(TypeError):
            Beer(id)

    def test_should_not_create_with_none_id(self):
        id = None
        name = BeerName.create('Boemia')
        with pytest.raises(AssertionError):
            Beer(id, name)

    def test_should_not_create_with_none_name(self):
        id = RefId.create(uuid.uuid4())
        name = None
        with pytest.raises(AssertionError):
            Beer(id, name)
