from beer_api.domain.repository.beer_repository import BeerRepository
from beer_api.domain.exceptions.beer_name_already_exists import BeerNameAlreadyExistsException

from beer_api.domain.entities.beer import Beer
from beer_api.domain.valueobjects.alcohol import Alcohol
from beer_api.domain.valueobjects.kind import Kind
from beer_api.domain.valueobjects.name import Name
from beer_api.domain.valueobjects.origin import Origin
from beer_api.domain.valueobjects.refid import RefId

from .beer_create_dto import CreateBeerDTO


class CreateBeerUseCase:

    def __init__(self, beer_repository: BeerRepository):
        self._beer_repository = beer_repository

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:

        id = str(RefId.new())
        name = Name.create(create_beer_dto.name)
        kind = Kind.create(create_beer_dto.kind)
        origin = Origin.create(create_beer_dto.origin)
        alcohol = Alcohol.create(create_beer_dto.alcohol)

        beer = self._beer_repository.find_by_name(name.value)

        if beer != None:
            raise BeerNameAlreadyExistsException

        beer = Beer(id=id, name=name, kind=kind,
                    origin=origin, alcohol=alcohol)

        return self._beer_repository.insert(beer)
