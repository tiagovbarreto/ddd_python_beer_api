import os
import tempfile
import pytest

from src.db import DB


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ['DATABASE_NAME'] = file_name

    DB.create_table(database_name=file_name)
    yield
    os.unlink(file_name)
