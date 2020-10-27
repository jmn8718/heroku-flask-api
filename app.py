from flask import Flask
from flask_restful import Resource, Api
import os
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from api.routes import initialize_routes

app = Flask(__name__)
api = Api(app)
port = int(os.environ.get('PORT', 5000))

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET', 'jwt_secret')
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

initialize_routes(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
