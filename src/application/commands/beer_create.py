from src.domain.entities.beer import Beer
from src.domain.usecases.create_beer import CreateBeerUseCase
from src.domain.usecases.beer_create_dto import CreateBeerDTO


class CreateBeerCommand:

    def __init__(self, create_beer_uc: CreateBeerUseCase):
        self._create_beer_uc = create_beer_uc

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
        return self._create_beer_uc.execute(create_beer_dto)
