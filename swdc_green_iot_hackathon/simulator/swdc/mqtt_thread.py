from mqtt_client import MqttClient

from PySide2 import QtCore
import json


class MqttThread(QtCore.QThread):

    open_partition = QtCore.Signal(str, str)

    def __init__(self, parent, container_id):
        super(MqttThread, self).__init__(parent)
        self.container_id = container_id


    def run(self):
        mqttc = MqttClient()
        mqttc.on_message = self.on_message
        mqttc.connect('broker.mqttdashboard.com', 1883)
        mqttc.subscribe('swdc/dispose/{}'.format(self.container_id), qos=1)
        mqttc.loop_start()

    def on_message(self, client, userdata, msg):
        print('message: {}'.format(msg.payload))
        for partition in json.loads(msg.payload):
            self.open_partition.emit(partition['partition_id'], partition['waste_type'])
