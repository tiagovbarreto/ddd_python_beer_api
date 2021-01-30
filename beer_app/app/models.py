import os
import sqlite3
import uuid

from typing import List
from pydantic import BaseModel, EmailStr, Field

class NotFound(Exception):
    pass

class Beer(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid:uuid4()))
    name: str
    brand: str
    alcohol: str

    @classmethod
    def get_by_id(cls, beer_id str):
        con: sqlite3.connection(os.getenv('DATABASE_NAME', 'database.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM articles WHERE id=? ', beer_id)

        record = cur.fechone()

        if record is None:
            raise NotFound

        beer = cls(**record)

        retur beer



