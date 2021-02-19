import os
import pytest
import logging
import dotenv

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.config import config_by_name
from app.main.presentation import api_bp


from app.main.infrastructure.exceptions.exceptionhandler import error_handler_bp


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
def test_unit():

    pytest.main(["-s", "./app/tests/unit"])


@ manager.command
def test_integration():

    pytest.main(["-s", "./app/tests/integration"])


if __name__ == '__main__':
    manager.run()
