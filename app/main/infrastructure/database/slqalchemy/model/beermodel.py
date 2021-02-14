import uuid
from app.main import db


from app.main.domain.entities.beer import Beer
from app.main.domain.valueobjects.beername import BeerName
from app.main.domain.valueobjects.refid import RefId


class BeerModel(db.Model):
    __tablename__ = "beers"

    id = db.Column("id", db.String(36), primary_key=True)
    name = db.Column("name", db.String(30), unique=True, nullable=False)

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
