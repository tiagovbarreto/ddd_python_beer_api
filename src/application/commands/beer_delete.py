from pydantic import BaseModel
from src.domain.models import Beer, NotFound


class AlreadyExists(Exception):
    pass


class DeleteBeerCommand(BaseModel):
    id: str

    def execute(self):

        beer = Beer.get_by_id(self.id)
        beer.delete()
