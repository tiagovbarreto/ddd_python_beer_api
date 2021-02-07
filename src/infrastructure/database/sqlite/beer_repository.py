import os
import sqlite3
from typing import List

from src.domain.repository.beer_repository import BeerRepository

from src.domain.entities.beer import Beer
from src.domain.valueobjects.name import Name
from src.domain.valueobjects.kind import Kind
from src.domain.valueobjects.origin import Origin
from src.domain.valueobjects.alcohol import Alcohol
from src.domain.valueobjects.refid import RefId

from src.domain.exceptions.entity_not_found import EntityNotFoundException


class SQLiteBeerRepository(BeerRepository):

    @classmethod
    def insert(cls, beer: Beer) -> Beer:
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO beers (id,name,kind,origin,alcohol) VALUES (?,?,?,?,?)",
                (beer.id, beer.name.value, beer.kind.value,
                 beer.origin.value, beer.alcohol.value)
            )
            con.commit()

        return beer

    @classmethod
    def update(cls, beer: Beer) -> Beer:
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:

            cur = con.cursor()
            cur.execute("UPDATE beers SET name=?, kind=?, origin=?, alcohol=? WHERE id=?",
                        (str(beer.name.value), beer.kind.value, beer.origin.value, beer.alcohol.value, beer.id.value))
            con.commit()

        return beer

    @classmethod
    def delete(cls, id: str) -> None:
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:
            sql = "DELETE FROM beers WHERE id=?"
            cur = con.cursor()
            cur.execute(sql, (id,))
            con.commit()

    @classmethod
    def find_by_id(cls, id: str):

        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM beers WHERE id=? ', (id,))

        record = cur.fetchone()

        if record is None:
            raise EntityNotFoundException

        beer = cls(**record)
        con.close()

        return beer

    @classmethod
    def find_all(cls) -> List['Beer']:
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM beers')

        records = cur.fetchall()
        beers = [cls(**record) for record in records]
        con.close()

        return beers

    @classmethod
    def find_by_name(cls, name: str):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM beers WHERE name = ?", (name,))

        record = cur.fetchone()

        if record is None:
            return None

        beer = cls(**record)
        con.close()

        return beer
