import abc
from src.domain.entities.beer import Beer
from src.domain.valueojbects.refid import RefId


class BeerRepository(abc.ABC):
    @abc.abstractmethod
    def insert(self, beer: Beer) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, beer: Beer) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, ref_id: RefId) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_ref_id(self, ref_id: RefId) -> Beer:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_all(self) -> [Beer]:
        raise NotImplementedError()
