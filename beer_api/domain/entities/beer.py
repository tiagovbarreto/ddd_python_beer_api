from dataclasses import dataclass

from beer_api.domain.valueobjects.refid import RefId
from beer_api.domain.valueobjects.beername import BeerName
from beer_api.domain.valueobjects.beerorigin import BeerOrigin


@dataclass(frozen=True)
class Beer:
    id: RefId
    name: BeerName
    origin: BeerOrigin

    def __post_init__(self):
        assert isinstance(
            self.id, RefId), "'id' must be an instance of RefId."
        assert isinstance(
            self.name, BeerName), "'name' must be an instance of BeerName."
        assert isinstance(
            self.origin, BeerOrigin), "'origin' must be an instance of BeerOrigin."
