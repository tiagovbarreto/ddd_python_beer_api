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
    type: str
    brand: str
    alcohol: str

    @classmethod
    def get_by_id(cls, beer_id str):
        conn: sqlite3.connection(os.getenv('DATABASE_NAME', 'database.db'))
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute('SELECT * FROM beer WHERE id=? ', beer_id)

        record = cur.fechone()

        if record is None:
            raise NotFound

        beer = cls(**record)
        conn.close()

        return beer

    @classmethod
    def list(cls) -> List['Beer']:
        conn: sqlite3.connection(os.getenv('DATABASE_NAME', 'database.db'))
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute('SELECT * FROM beer', beer_id)

        record = cur.fechall()
        beers = [ls(**record) for record in records]
        conn.close()

        return beers

    @classmethod
    def save(cls) -> 'Beer':
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'database.db')) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSET INTO beer (id, name, type, origin, alcoholic) VALUES (?,?,?,?,?)"),
                (self.id, self.name, self.type, self.origin, self.alcoholic)
            )    
            conn.commit()
    
        return self

    @classmethod
    def create_table(cls, database_name= 'database.db'):
        conn = sqlite3.connect(database_name)
        
        conn.execute(
            "CREATE TABLE IF NOT EXISTS beer (id NUMBER, name TEXT, type TEXT, origin TEXT,  alcoholic TEXT)")

        conn.close()
