import sqlite3


class DB:

    @ classmethod
    def create_table(cls, database_name='database.db'):
        con = sqlite3.connect(database_name)

        con.execute(
            "CREATE TABLE IF NOT EXISTS beers (id TEXT, name TEXT, kind TEXT, origin TEXT,  alcohol TEXT)")

        con.close()
