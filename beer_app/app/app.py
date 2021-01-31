from flask import Flask, jsonify, request

from app.commands import CreateBeerCommand
from app.queries import GetBeerByIDQuery, ListBeerQuery

app = Flask(__name__)


@app.route('/beers', methods=['POST'])
def create_beer():
    cmd = CreateBeerCommand(
        **request.json
    )
    return jsonify(cmd.execute().dict())


if __name__ == '__main__':
    app.run()
