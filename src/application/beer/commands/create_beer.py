from pydantic import BaseModel
from src.domain.models import Beer, NotFound
from src.domain.usecases.create_beer import CreateBeerUseCase


class AlreadyExists(Exception):
    pass


class CreateBeerCommand:

     def __init__(self, create_beer_uc: CreateBeerCommand):
        self._create_beer_uc = create_beer_uc

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
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
