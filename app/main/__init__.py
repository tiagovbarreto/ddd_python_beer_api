from flask import Flask

from app.main.config import config_by_name
from app.main.database import db
from app.main.presentation import api_bp
from app.main.infrastructure.exceptions.exceptionhandler import error_handler_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    app.register_blueprint(api_bp)
    app.register_blueprint(error_handler_bp)

    db.init_app(app)

    return app


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
