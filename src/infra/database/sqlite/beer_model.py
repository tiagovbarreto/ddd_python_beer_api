import uuid

from pydantic import BaseModel, Field
from src.domain.entities.beer import Beer
from src.domain.valueojbects.name import Name
from src.domain.valueojbects.kind import Kind
from src.domain.valueojbects.origin import Origin
from src.domain.valueojbects.alcohol import Alcohol
from src.domain.valueojbects.refid import RefId


class BeerModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    kind: str
    origin: str
    alcohol: str

    @classmethod
    def create_from(cls, beer: Beer) -> "BeerModel":
        return BeerModel(
            id=beer.id.value.hex,
            name=beer.name.value,
            kind=beer.kind.value,
            origin=beer.origin.value,
            alcohol=beer.alcohol.value
        )

    def to_entity(self) -> Beer:
        id = RefId.create(uuid.UUID(self.ref_id, version=4))
        name = Name.create(self.username)
        kind = Kind.create(self.username)
        origin = Origin.create(self.username)
        alcohol = Alcohol.create(self.username)

        return Beer(id, name, kind, origin, alcohol
