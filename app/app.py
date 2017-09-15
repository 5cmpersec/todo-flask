from flask import Flask
from flask_restful import Api

from app.api.resources.task_list import TaskList
from app.api.resources.task import Task

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

api = Api(app)

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:id>')
