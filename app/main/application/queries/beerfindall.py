from typing import List
from main.domain.entities.beer import Beer


class FindAllBeerQuery:
    def execute(self) -> List[Beer]:
        pass
