from flask_restful import Resource
from flask import request, json

from mqtt_thread import MqttThread


class WasteCollector(Resource):

    waste_partition = {
        'plastic': 'partition1',
        'cardboard': 'partition2',
    }

    def post(self):
        if not request.json:
            return 'Wrong request type, expected json data'

        partitions = []

        for waste_type in request.json['waste_contents']:
            if waste_type in self.waste_partition:
                partitions.append({
                    'partition_id': self.waste_partition[waste_type],
                    'waste_type': waste_type,
                })

        topic = 'swdc/dispose/' + request.json['container_id']
        message = json.dumps(partitions)
        
        thread = MqttThread(topic, message)
        thread.start()
        thread.join()
        
        return 'Recieved Data'
        