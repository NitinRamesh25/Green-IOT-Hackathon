from flask import Flask
from flask_restful import Api

from waste_collector import WasteCollector
from keep_alive import KeepAlive

app = Flask(__name__)
api = Api(app)
api.add_resource(WasteCollector, '/dispose')
api.add_resource(KeepAlive, '/')


if __name__ == '__main__':
    app.run(debug=False)
