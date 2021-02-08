from pydantic import BaseModel
from beer_api.domain.models import Beer, NotFound


class UpdateBeerCommand(BaseModel):
    id: str
    data: Beer

    def execute(self) -> Beer:
        try:
            Beer.get_by_name(self.data.name)
            raise AlreadyExists
        except NotFound:
            pass

        beer = Beer.get_by_id(self.id)
        beer.name = self.data.name
        beer.kind = self.data.kind
        beer.origin = self.data.origin
        beer.alcohol = self.data.alcohol

        beer.update()

        return beer
