import sqlite3
from typing import List
from contextlib import contextmanager

from beer_api.domain.repository.beer_repository import BeerRepository

from beer_api.domain.entities.beer import Beer
from beer_api.domain.valueobjects.name import Name
from beer_api.domain.valueobjects.kind import Kind
from beer_api.domain.valueobjects.origin import Origin
from beer_api.domain.valueobjects.alcohol import Alcohol
from beer_api.domain.valueobjects.refid import RefId

from beer_api.domain.exceptions.entity_not_found import EntityNotFoundException


class SQLiteBeerRepository(BeerRepository):
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
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO beers (id,name,kind,origin,alcohol) VALUES (?,?,?,?,?)",
                (
                    beer.id,
                    beer.name.value,
                    beer.kind.value,
                    beer.origin.value,
                    beer.alcohol.value,
                ),
            )
            con.commit()

        return beer

    def update(self, beer: Beer) -> Beer:
        with self._connect() as con:

            cur = con.cursor()
            cur.execute(
                "UPDATE beers SET name=?, kind=?, origin=?, alcohol=? WHERE id=?",
                (
                    str(beer.name.value),
                    beer.kind.value,
                    beer.origin.value,
                    beer.alcohol.value,
                    beer.id.value,
                ),
            )
            con.commit()

        return beer

    def delete(self, id: str) -> None:
        with self._connect() as con:
            sql = "DELETE FROM beers WHERE id=?"
            cur = con.cursor()
            cur.execute(sql, (id,))
            con.commit()

    def find_by_id(self, id: str) -> Beer:
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
        with self._connect() as con:
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM beers")

            records = cur.fetchall()
            beers = [Beer(**record) for record in records]

            return beers

    def find_by_name(self, name: str) -> Beer:
        with self._connect() as con:
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM beers WHERE name = ?", (name,))

            record = cur.fetchone()

            if record is None:
                return None

            beer = Beer(**record)

            return beer
