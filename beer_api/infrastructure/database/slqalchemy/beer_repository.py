import logging
from beer_api.domain.repository.beer_repository import BeerRepository
from beer_api.domain.entities.beer import Beer
from .config import session
from .beer_model import BeerModel


_logger = logging.Logger(__name__)


class SQLAlchemyRepository(BeerRepository):
    def insert(self, beer: Beer) -> None:
        _logger.debug(f"Preparing to insert Beer:{beer}")

        model = BeerModel.create_from(beer)
        session.add(model)
        session.commit()

    def update(self, beer: Beer) -> None:
        pass

    def delete(self, ref_id: RefId) -> None:
        pass

    def get_by_ref_id(self, ref_id: RefId) -> User:
        _logger.debug(f"Preparing to get User by ref ID:{ref_id}")

        model = session.query(UserModel).get(str(ref_id))

        if model:
            return model.to_entity()

        return None

    def list_all(self) -> [User]:
        _logger.debug(f"Preparing to list all Users")

        result = session.query(UserModel).all()

        if result:
            return [model.to_entity() for model in result]

        return None
