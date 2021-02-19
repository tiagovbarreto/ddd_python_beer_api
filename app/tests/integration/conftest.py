import pytest
from app.main import create_app
from app.main.database import db

config = 'tst'


@pytest.fixture
def client():
    _app = create_app(config)

    with _app.test_client() as client:
        with _app.app_context():
            # init database
            db.drop_all()
            db.create_all()
        yield client


@pytest.fixture
def app():
    return create_app('tst')
