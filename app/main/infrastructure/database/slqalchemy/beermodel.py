import uuid
from sqlalchemy import Column, String, Table, ForeignKey
from .config import Base

from main.domain.entities.beer import Beer
from main.domain.valueobjects.beername import BeerName
from main.domain.valueobjects.refid import RefId


class BeerModel(Base):
    __tablename__ = "beers"

    id = Column("id", String(36), primary_key=True)
    name = Column("name", String(50), unique=True, nullable=False)

    @classmethod
    def create_from(cls, beer: Beer) -> "BeerModel":
        return BeerModel(
            id=beer.id.value.hex,
            name=beer.name.value,
        )

    def to_entity(self) -> Beer:
        id = RefId.create(uuid.UUID(self.id, version=4))
        name = BeerName.create(self.name)

        return Beer(id, name)
