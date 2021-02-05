from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f"sqlite:///:memory:")
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

Base = declarative_base()


def create_database():
    Base.metadata.create_all(engine)


def drop_database():
    Base.metadata.drop_all(engine)
