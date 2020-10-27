from .Auth import Auth
from .Status import Status
from .Health import Health
from .Todo import Todo, TodoList

def initialize_routes(api):
    api.add_resource(Status, '/')
    api.add_resource(Auth, '/auth')
    api.add_resource(Health, '/health')
    api.add_resource(TodoList, '/todos')
    api.add_resource(Todo, '/todos/<string:todo_id>')
