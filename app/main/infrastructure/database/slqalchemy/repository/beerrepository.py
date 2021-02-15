import logging
from app.main.domain.repository.beerrepository import BeerRepository
from app.main.domain.entities.beer import Beer
from app.main.domain.valueobjects.refid import RefId
from app.main import db
from ..model.beermodel import BeerModel


_logger = logging.Logger(__name__)


class SQLACBeerRepository(BeerRepository):

    # @property
    # @classmethod
    # @abc.abstractmethod
    # TYPE = "SQLACBeerRepository"

    def insert(self, beer: Beer) -> Beer:
        _logger.debug(f"Preparing to insert Beer:{beer}")

        model = BeerModel.create_from(beer)
        db.session.add(model)
        db.session.commit()

    def update(self, beer: Beer) -> 'Beer':
        pass

    def delete(self, id: RefId) -> None:
        pass

    def find_by_id(self, id: RefId) -> Beer:
        _logger.debug(f"Preparing to find Beer by id:{id}")

        model = db.session.query(BeerModel).get(id.value.hex)

        if model:
            return model.to_entity()

        return None

    def find_all(self) -> [Beer]:
        _logger.debug(f"Preparing to list all Beers")

        result = db.session.query(BeerModel).all()

        if result:
            return [model.to_entity() for model in result]

        return None

    def find_by_name(self, name: str) -> Beer:
        _logger.debug(f"Preparing to find Beer by name:{name}")

        model = BeerModel.query.filter_by(name=name).first()

        if model:
            return model.to_entity()

        return None
