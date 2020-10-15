from flask import Flask
from flask_restful import Resource, Api
import os

from api.Status import Status
from api.Health import Health
from api.Todo import Todo, TodoList

app = Flask(__name__)
api = Api(app)
port = int(os.environ.get('PORT', 5000))

api.add_resource(Status, '/')
api.add_resource(Health, '/health')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)