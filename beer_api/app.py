from flask import Flask
from beer_api.presentation import api

app = Flask(__name__)
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)


# TODO Add logs
# TODO add error handlers
