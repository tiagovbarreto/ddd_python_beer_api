import uuid
from sqlalchemy import Column, String, Table, ForeignKey
from .config import Base

from src.domain.entities.beer import Beer
from src.domain.valueojbects.name import Name
from src.domain.valueojbects.kind import Kind
from src.domain.valueojbects.origin import Origin
from src.domain.valueojbects.alcohol import Alcohol
from src.domain.valueojbects.refid import RefId


class BeerModel(Base):
    __tablename__ = "beers"

    ref_id = Column("id", String(36), primary_key=True)
    name = Column("name", String(50), unique=True, nullable=False)
    kind = Column("kind", String(20), nullable=False)
    origin = Column("origin", String(30), nullable=False)
    alcohol = Column("alcohol", String(20), nullable=False)

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

        return Beer(id, name, kind, origin, alcohol)
