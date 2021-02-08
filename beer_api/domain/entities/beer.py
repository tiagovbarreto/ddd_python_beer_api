from dataclasses import dataclass

from beer_api.domain.valueobjects.alcohol import Alcohol
from beer_api.domain.valueobjects.kind import Kind
from beer_api.domain.valueobjects.name import Name
from beer_api.domain.valueobjects.origin import Origin
from beer_api.domain.valueobjects.refid import RefId


@dataclass(frozen=True)
class Beer:
    id: RefId
    alcohol: Alcohol
    kind: Kind
    name: Name
    origin: Origin

    def __post_init__(self):
        assert isinstance(
            self.name, Name), "'name' must be an instance of Name."
        assert isinstance(
            self.kind, Kind), "'kind' must be an instance of Kind."
        assert isinstance(
            self.origin, Origin), "'origin' must be an instance of Origin."
        assert isinstance(
            self.alcohol, Alcohol), "'alcohol' must be an instance of Acohol."
