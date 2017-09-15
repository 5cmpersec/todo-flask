from flask_restful import Resource

class TaskList(Resource):
    def get(self):
        return {"get" : "TaskList"}

    def post(self):
        return {"post" : "TaskList"}
