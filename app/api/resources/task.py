from flask_restful import Resource

class Task(Resource):
    def get(self, id):
        return {"get" : id}

    def put(self, id):
        return {"put" : id }

    def delete(self, id):
        return {"delete" : id}
