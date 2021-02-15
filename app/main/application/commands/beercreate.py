import logging

from app.main.domain.entities.beer import Beer
from app.main.domain.usecases.createbeer import CreateBeerUseCase
from app.main.domain.usecases.beercreatedto import CreateBeerDTO

_logger = logging.Logger(__name__)


class CreateBeerCommand:

    def __init__(self, create_beer_uc: CreateBeerUseCase):
        self._create_beer_uc = create_beer_uc

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
        _logger.debug(f"Execute create_beer_dto:{create_beer_dto}")

        return self._create_beer_uc.execute(create_beer_dto)
