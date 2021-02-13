import sqlite3
import logging

from typing import List
from contextlib import contextmanager

from app.main.domain.entities.beer import Beer
from app.main.domain.valueobjects.beername import BeerName
from app.main.domain.valueobjects.refidimport RefId
from app.main.domain.repository.beerrepository import BeerRepository
from app.main.domain.exceptions.entitynotfound import EntityNotFoundException

_logger = logging.Logger(__name__)


class SQLiteBeerRepository(BeerRepository):

    TYPE = "SQLiteBeerRepository"

    def __init__(self, database: str):
        self._database = database

    @contextmanager
    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._database)
        try:
            yield connection
        finally:
            connection.close()

    def insert(self, beer: Beer) -> Beer:
        _logger.debug(f"Preparing to insert Beer: {beer}")

        with self._connect() as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO beers (id,name) VALUES (?,?)",
                (
                    beer.id.hex,
                    beer.name.value,
                ),
            )
            con.commit()

        return beer

    def update(self, beer: Beer) -> Beer:
        _logger.debug(f"Preparing to update Beer: {beer}")

        with self._connect() as con:

            cur = con.cursor()
            cur.execute(
                "UPDATE beers SET name=? WHERE id=?",
                (
                    beer.name.value,
                    beer.id.value,
                ),
            )
            con.commit()

        return beer

    def delete(self, id: str) -> None:
        _logger.debug(f"Preparing to delete Beer with id:{id}")

        with self._connect() as con:
            sql = "DELETE FROM beers WHERE id=?"
            cur = con.cursor()
            cur.execute(sql, (id,))
            con.commit()

    def find_by_id(self, id: str) -> Beer:
        _logger.debug(f"Preparing to find Beer by id:{id}")

        with self._connect() as con:
            cur = con.cursor()
            con.row_factory = sqlite3.Row

            cur.execute("SELECT * FROM beers WHERE id=? ", (id,))

            record = cur.fetchone()

            if record is None:
                raise EntityNotFoundException

            beer = Beer(**record)

            return beer

    def find_all(self) -> List[Beer]:
        _logger.debug(f"Preparing to find all Beers")

        with self._connect() as con:
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM beers")

            records = cur.fetchall()
            beers = [Beer(**record) for record in records]

            return beers

    def find_by_name(self, name: str) -> Beer:
        _logger.debug(f"Preparing to find Beer by name: {name}")

        with self._connect() as con:
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM beers WHERE name = ?", (name,))

            record = cur.fetchone()

            if record is None:
                return None

            beer = Beer(**record)

            return beer
