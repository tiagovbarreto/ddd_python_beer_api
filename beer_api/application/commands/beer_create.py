from beer_api.domain.entities.beer import Beer
from beer_api.domain.usecases.create_beer import CreateBeerUseCase
from beer_api.domain.usecases.beer_create_dto import CreateBeerDTO


class CreateBeerCommand:

    def __init__(self, create_beer_uc: CreateBeerUseCase):
        self._create_beer_uc = create_beer_uc

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
        return self._create_beer_uc.execute(create_beer_dto)
