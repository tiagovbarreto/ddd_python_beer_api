import pytest
from app.main import create_app
from app.main.database import db

config = 'tst'


@pytest.fixture
def client():
    app = create_app(config)

    with app.test_client() as client:
        with app.app_context():
            # init database
            db.drop_all()
            db.create_all()
        yield client
