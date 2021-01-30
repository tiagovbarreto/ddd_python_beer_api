from typing import List
from pydantic import BaseModel
from app.models import Beer


class ListBeerQuery(BaseModel):
    def execute(self) -> List[Beer]:
        beers = Beer.list()

        return beers


class GetBeerByIDQuery(BaseModel):
    id: str

    def execute(self) -> Beer:
        beer = Beer.get_by_id(self.id)

        return beer
