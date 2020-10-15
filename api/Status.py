from flask import Flask
from flask_restful import Resource, Api

class Status(Resource):
    def get(self):
        return {'status': True}