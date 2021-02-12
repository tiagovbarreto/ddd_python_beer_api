import logging
from main.domain.repository.beerrepository import BeerRepository
from main.domain.entities.beer import Beer
from main.domain.valueobjects.refid import RefId
from .config import session
from .beermodel import BeerModel


_logger = logging.Logger(__name__)


class SQLACBeerRepository(BeerRepository):
    def insert(self, beer: Beer) -> Beer:
        _logger.debug(f"Preparing to insert Beer:{beer}")

        model = BeerModel.create_from(beer)
        session.add(model)
        session.commit()

    def update(self, beer: Beer) -> 'Beer':
        pass

    def delete(self, id: RefId) -> None:
        pass

    def find_by_id(self, id: RefId) -> Beer:
        _logger.debug(f"Preparing to find Beer by id:{id}")

        model = session.query(BeerModel).get(str(id))

        if model:
            return model.to_entity()

        return None

    def find_all(self) -> [Beer]:
        _logger.debug(f"Preparing to list all Beers")

        result = session.query(BeerModel).all()

        if result:
            return [model.to_entity() for model in result]

        return None

    def find_by_name(self, name: str) -> Beer:
        return None
