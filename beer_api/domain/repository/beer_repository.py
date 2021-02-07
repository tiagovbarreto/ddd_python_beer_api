import abc
from beer_api.domain.entities.beer import Beer
from beer_api.domain.valueobjects.refid import RefId


class BeerRepository(abc.ABC):
    @abc.abstractmethod
    def insert(self, beer: Beer) -> Beer:
        pass

    @abc.abstractmethod
    def update(self, beer: Beer) -> Beer:
        pass

    @abc.abstractmethod
    def delete(self, ref_id: RefId) -> None:
        pass

    @abc.abstractmethod
    def find_by_id(self, ref_id: RefId) -> Beer:
        pass

    @abc.abstractmethod
    def find_all(self) -> [Beer]:
        pass
