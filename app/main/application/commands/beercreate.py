from app.main.domain.entities.beer import Beer
from app.main.domain.usecases.createbeer import CreateBeerUseCase
from app.main.domain.usecases.beercreatedto import CreateBeerDTO


class CreateBeerCommand:

    def __init__(self, create_beer_uc: CreateBeerUseCase):
        self._create_beer_uc = create_beer_uc

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
        return self._create_beer_uc.execute(create_beer_dto)
