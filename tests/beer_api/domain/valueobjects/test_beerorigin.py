import pytest
import uuid
from beer_api.domain.valueobjects.beerorigin import BeerOrigin


class TestBeerOrigin:

    def test_should_create(self):
        beer_origin = 'Brasil'
        instance = BeerOrigin.create(beer_origin)
        assert isinstance(instance, BeerOrigin)
        assert instance.value == beer_origin 

    def test_should_not_create_from_constructor_passing_none(self):
        beer_origin = 'Brasil'
        with pytest.raises(AssertionError):
            BeerOrigin(beer_origin, None)
    
    def test_should_not_create_from_constructor_passing_object(self):
        beer_origin = 'Brasil'
        with pytest.raises(AssertionError):
            BeerOrigin(beer_origin, object())
    
    def test_should_not_create_from_none(self):
        beer_origin = None
        with pytest.raises(ValueError):
            BeerOrigin.create(beer_origin)

    def test_should_not_create_from_empty(self):
        beer_origin = ""
        with pytest.raises(ValueError):
            BeerOrigin.create(beer_origin)
    
    def test_should_not_create_from_empty_with_blank_spaces(self):
        beer_origin = "  "
        with pytest.raises(ValueError):
            BeerOrigin.create(beer_origin)
    
    def test_should_not_create_beerorigin_with_length_less_than_three_characteres(self):
        beer_origin = "be"
        with pytest.raises(ValueError):
            BeerOrigin.create(beer_origin)
    
    def test_should_not_create_beerorigin_with_length_greater_than_thirty_characteres(self):
        beer_origin = "this_is_not_a_good_origin_name_for_beer"
        with pytest.raises(ValueError):
            BeerOrigin.create(beer_origin)