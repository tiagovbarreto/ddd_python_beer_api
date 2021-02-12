from app.maindoapp.mainentities.beer import Beer
from app.maindoapp.mainusecases.createbeer import CreateBeerUseCase
from app.maindoapp.mainusecases.beercreatedto import CreateBeerDTO


class CreateBeerCommand:

    def __init__(self, create_beer_uc: CreateBeerUseCase):
        self._create_beer_uc = create_beer_uc

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
        return self._create_beer_uc.execute(create_beer_dto)
