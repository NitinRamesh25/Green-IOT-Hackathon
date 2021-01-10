from flask_restful import Resource


class KeepAlive(Resource):
    def get(self):
        return "KeepAlive"
