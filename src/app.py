from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields

from src.apis import api

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run()
