from flask import Flask, Blueprint
from main.presentation import api
#from flask_restful import Resource, Api

app = Flask(__name__)
api.init_app(app)
# bp = Blueprint('api', __name__)
# api = Api(bp)


# class Student(Resource):
#     def get(self, name):
#         return {'student': name}


# api.add_resource(Student, '/student/<string:name>')
# app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)


# TODO Add logs
# TODO add error handlers
