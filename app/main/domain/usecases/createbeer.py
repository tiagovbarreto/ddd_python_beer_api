import logging

from app.main.domain.repository.beerrepository import BeerRepository
from app.main.domain.exceptions.beernamealreadyexists import BeerNameAlreadyExistsException

from app.main.domain.entities.beer import Beer
from app.main.domain.valueobjects.refid import RefId
from app.main.domain.valueobjects.beername import BeerName

from .beercreatedto import CreateBeerDTO

_logger = logging.Logger(__name__)


class CreateBeerUseCase:

    def __init__(self, beer_repository: BeerRepository):
        self._beer_repository = beer_repository

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:

        _logger.debug(f"Execute create_beer_dto:{create_beer_dto}")

        id = RefId.new()
        name = BeerName.create(create_beer_dto.name)

        beer = self._beer_repository.find_by_name(name.value)

        if beer != None:
            raise BeerNameAlreadyExistsException(name.value)

        beer = Beer(id=id, name=name)

        return self._beer_repository.insert(beer)
