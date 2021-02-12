from dataclasses import dataclass

from main.domain.valueobjects.refid import RefId
from main.domain.valueobjects.beername import BeerName


@dataclass(frozen=True)
class Beer:
    id: RefId
    name: BeerName

    def __post_init__(self):
        assert isinstance(
            self.id, RefId), "'id' must be an instance of RefId."
        assert isinstance(
            self.name, BeerName), "'name' must be an instance of BeerName."
