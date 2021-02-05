from src.domain.repository.beer_repository import BeerRepository
from src.domain.errors.repository_error import RepositoryError


class CreateBeerUseCase:
    def __init__(self, beer_repository: BeerRepository):
        self._beer_repository = beer_repository

    def execute(self, create_beer_dto: CreateBeerDTO) -> Beer:
        name = Name.create(create_beer_dto.name)
        kind = Kind.create(create_beer_dto.kind)
        origin = Origin.create(create_beer_dto.origin)
        name = Name.create(create_beer_dto.name)
        name = Name.create(create_beer_dto.name)
        ref_id = RefId.new()

        user = User(ref_id=ref_id, username=username)
        try:
            self._user_repository.insert(user)
        except Exception as ex:
            class_name = self.__class__.__name__
            raise RepositoryError(repository=class_name, message=ex)

        return CreateUserResponse(str(ref_id.value))
