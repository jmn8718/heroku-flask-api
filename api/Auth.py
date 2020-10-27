from flask import Flask, jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token
)


class Auth(Resource):
    # only allow price changes, no name changes allowed
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help='Username is missing')
    parser.add_argument('password', type=str, required=True,
                        help='Password is missing')

    # TODO implement user authentication
    def post(self):
        data = Auth.parser.parse_args()

        access_token = create_access_token(identity=data['username'])
        return {"access_token": access_token}, 200
