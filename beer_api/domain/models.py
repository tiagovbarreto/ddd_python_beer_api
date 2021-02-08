import os
import sqlite3
import uuid

from typing import List
from pydantic import BaseModel, Field


class NotFound(Exception):
    pass


class Beer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    kind: str
    origin: str
    alcohol: str

    @classmethod
    def get_by_id(cls, beer_id: str):

        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM beers WHERE id=? ", (beer_id,))

        record = cur.fetchone()

        if record is None:
            raise NotFound

        beer = cls(**record)
        con.close()

        return beer

    @classmethod
    def get_by_name(cls, name: str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
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
    def list(cls) -> List["Beer"]:
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM beers")

        records = cur.fetchall()
        beers = [cls(**record) for record in records]
        con.close()

        return beers

    def save(self) -> "Beer":
        with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO beers (id,name,kind,origin,alcohol) VALUES (?,?,?,?,?)",
                (self.id, self.name, self.kind, self.origin, self.alcohol),
            )
            con.commit()

        return self

    def update(self) -> "Beer":
        with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as con:

            cur = con.cursor()
            cur.execute(
                "UPDATE beers SET name=?, kind=?, origin=?, alcohol=? WHERE id=?",
                (self.name, self.kind, self.origin, self.alcohol, self.id),
            )
            con.commit()

        return self

    def delete(self):
        with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as con:
            print(f"{self.id}")
            sql = "DELETE FROM beers WHERE id=?"
            cur = con.cursor()
            cur.execute(sql, (self.id,))
            con.commit()
