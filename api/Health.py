from flask import Flask
from flask_restful import Resource, Api

class Health(Resource):
    def get(self):
        return {'status': True}