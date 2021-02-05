from dataclasses import dataclass
from src.domain.valueobjects import Name, Kind, Origin, Alcohol


@dataclass(frozen=True)
class Beer():
    __create_key = object()

    id: RefId
    name: Name
    kind: Kind
    origin: Origin
    alcohol: Alcohol

    def __post_init__(self):
        assert isinstance(name, Name), "'name' must be an instance of Name."
        assert isinstance(kind, Kind), "'kind' must be an instance of Kind."
        assert isinstance(
            origin, Origin), "'origin' must be an instance of Origin."
        assert isinstance(
            alcohol, Alcohol), "'alcohol' must be an instance of Acohol."
