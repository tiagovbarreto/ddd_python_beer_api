import os
import pytest
import logging
import dotenv

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app
from app.main.database import db

# from app.main.infrastructure.database.slqalchemy.model.beermodel import BeerModel

_logger = logging.Logger(__name__)

app = create_app('dev')
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@ manager.command
def run():
    app.run()


@ manager.command
def test():

    pytest.main(["-s", "./app/tests"])


@ manager.command
def test_unit():

    pytest.main(["-s", "./app/tests/unit"])


@ manager.command
def test_integration():

    pytest.main(["-s", "./app/tests/integration"])


if __name__ == '__main__':
    manager.run()
