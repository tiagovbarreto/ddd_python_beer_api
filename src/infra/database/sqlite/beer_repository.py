import os
import sqlite3
import uuid

from typing import List
from pydantic import BaseModel, Field

from .beer_repository import BeerRepository

from src.domain.entities.beer import Beer
from src.domain.valueojbects.name import Name
from src.domain.valueojbects.kind import Kind
from src.domain.valueojbects.origin import Origin
from src.domain.valueojbects.alcohol import Alcohol
from src.domain.valueojbects.refid import RefId


class SQLiteRepository(BeerRepository):

    def insert(self) -> 'Beer':
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO beers (id,name,kind,origin,alcohol) VALUES (?,?,?,?,?)",
                (self.id, self.name, self.kind, self.origin, self.alcohol)
            )
            con.commit()

        return self

    @classmethod
    def get_by_id(cls, beer_id: str):

        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM beers WHERE id=? ', (beer_id,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        beer = cls(**record)
        con.close()

        return beer

    @classmethod
    def get_by_name(cls, name: str):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM beers WHERE name = ?", (name,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        beer = cls(**record)  # Row can be unpacked as dict
        con.close()

        return beer

    @classmethod
    def list(cls) -> List['Beer']:
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM beers')

        records = cur.fetchall()
        beers = [cls(**record) for record in records]
        con.close()

        return beers

    def save(self) -> 'Beer':
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO beers (id,name,kind,origin,alcohol) VALUES (?,?,?,?,?)",
                (self.id, self.name, self.kind, self.origin, self.alcohol)
            )
            con.commit()

        return self

    def update(self) -> 'Beer':
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:

            cur = con.cursor()
            cur.execute("UPDATE beers SET name=?, kind=?, origin=?, alcohol=? WHERE id=?",
                        (self.name, self.kind, self.origin, self.alcohol, self.id))
            con.commit()

        return self

    def delete(self):
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as con:
            print(f'{self.id}')
            sql = "DELETE FROM beers WHERE id=?"
            cur = con.cursor()
            cur.execute(sql, (self.id,))
            con.commit()

    @ classmethod
    def create_table(cls, database_name='database.db'):
        con = sqlite3.connect(database_name)

        con.execute(
            "CREATE TABLE IF NOT EXISTS beers (id TEXT, name TEXT, kind TEXT, origin TEXT,  alcohol TEXT)")

        con.close()
