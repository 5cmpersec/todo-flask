from flask import Flask
from flask_restful import Api

from app.api.resources.foo import Foo

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

api = Api(app)

api.add_resource(Foo, '/Foo')
