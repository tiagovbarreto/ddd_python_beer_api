import abc
from app.main.domain.entities.beer import Beer
from app.main.domain.valueobjects.refid import RefId


class BeerRepository(abc.ABC):

    # @property
    # @classmethod
    # @abc.abstractmethod
    # def TYPE(cls):
    #     return NotImplementedError

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

    @abc.abstractmethod
    def find_by_name(self, name: str) -> Beer:
        pass
