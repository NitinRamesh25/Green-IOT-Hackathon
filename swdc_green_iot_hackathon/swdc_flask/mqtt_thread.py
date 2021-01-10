import threading
from mqtt_client import MqttClient


class MqttThread(threading.Thread):

    def __init__(self, topic, message):
        threading.Thread.__init__(self)
        self.topic = topic
        self.message = message

    def run(self):
        self.mqttc = MqttClient()
        self.mqttc.connect('broker.mqttdashboard.com', 1883)
        self.mqttc.publish(self.topic, self.message, qos=1)
        self.mqttc.loop_start()
