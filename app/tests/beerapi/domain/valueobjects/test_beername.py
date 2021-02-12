import pytest
import uuid
from main.domain.valueobjects.beername import BeerName


class TestBeerName:

    def test_should_create(self):
        beer_name = 'Eisenbahn'
        instance = BeerName.create(beer_name)
        assert isinstance(instance, BeerName)
        assert instance.value == beer_name

    def test_should_not_create_from_constructor_passing_none(self):
        beer_name = 'Eisenbahn'
        with pytest.raises(AssertionError):
            BeerName(beer_name, None)

    def test_should_not_create_from_constructor_passing_object(self):
        beer_name = 'Eisenbahn'
        with pytest.raises(AssertionError):
            BeerName(beer_name, object())

    def test_should_not_create_from_none(self):
        beer_name = None
        with pytest.raises(ValueError):
            BeerName.create(beer_name)

    def test_should_not_create_from_empty(self):
        beer_name = ""
        with pytest.raises(ValueError):
            BeerName.create(beer_name)

    def test_should_not_create_from_empty_with_blank_spaces(self):
        beer_name = "  "
        with pytest.raises(ValueError):
            BeerName.create(beer_name)

    def test_should_not_create_beername_with_length_less_than_three_characteres(self):
        beer_name = "be"
        with pytest.raises(ValueError):
            BeerName.create(beer_name)

    def test_should_not_create_beername_with_length_greater_than_twenty_characteres(self):
        beer_name = "not_good_name_for_beer"
        with pytest.raises(ValueError):
            BeerName.create(beer_name)
