from pydantic import BaseModel
from app.models import Beer, NotFound


class AlreadyExists(Exception):
    pass


class CreateBeerCommand(BaseModel):
    name: str
    kind: str
    origin: str
    alcohol: str

    def execute(self) -> Beer:
        try:
            Beer.get_by_name(self.name)
            raise AlreadyExists
        except NotFound:
            pass

        beer = Beer(
            name=self.name,
            kind=self.kind,
            origin=self.origin,
            alcohol=self.alcohol
        )

        beer.save()

        return beer
