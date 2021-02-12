from main.domain.repository.beerrepository import BeerRepository
from main.domain.exceptions.beernamealreadyexists import BeerNameAlreadyExistsException

from main.domain.entities.beer import Beer
from main.domain.valueobjects.refid import RefId
from main.domain.valueobjects.beername import BeerName

from .beercreatedto import CreateBeerDTO


class CreateBeerUseCase:

    def __init__(self, beer_repository: BeerRepository):
        self._beer_repository = beer_repository

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:

        id = RefId.new()
        name = BeerName.create(create_beer_dto.name)

        beer = self._beer_repository.find_by_name(name.value)

        if beer != None:
            raise BeerNameAlreadyExistsException

        beer = Beer(id=id, name=name)

        return self._beer_repository.insert(beer)
