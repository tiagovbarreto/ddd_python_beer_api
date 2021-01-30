from typing import List
from pydantic import BaseModel
from app.models import Beer


class ListBeerQuery(BaseModel):
    def execute(self) -> List[Beer]:
        beers = Beer.list()

        return beers
