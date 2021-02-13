from app.main.infrastructure.database.slqalchemy.repository.beerrepository import SQLACBeerRepository
from app.main.infrastructure.database.sqlite.repository.beerrepository import SQLiteBeerRepository


class RepositoryFactory:

    @classmethod
    def create_repository(type: str):
        if(SQLiteBeerRepository.TYPE == type):
            return new SQLiteBeerRepository()
        elif(SQLACBeerRepositor.TYPE == type):
            return new SQLACBeerRepository()
