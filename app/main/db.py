import sqlite3


class DB:
    @classmethod
    def create_table(cls, database_name):
        con = sqlite3.connect(database_name)

        con.execute(
            "CREATE TABLE IF NOT EXISTS beers (id TEXT, name TEXT)"
        )

        con.close()
