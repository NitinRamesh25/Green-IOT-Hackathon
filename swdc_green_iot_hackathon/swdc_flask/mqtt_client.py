import paho.mqtt.client as paho
import threading

paho_client = paho.Client()

class MqttClient(paho.Client):

    def __init__(self):
        super(MqttClient, self).__init__()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('Client: Connected')
        elif rc == 1:
            print('Client: Incorrect protocol version')
        elif rc == 2:
            print('Client: Invalid client identifier')
        elif rc == 3:
            print('Client: Server unavailable')
        elif rc == 4:
            print('Client: Bad username or password')
        elif rc == 5:
            print('Client: Not Authorized')
        else:
            print('Client: Something went wrong')


    def on_publish(self, client, userdata, mid):
        print('published: {}'.format(str(mid)))
        self.disconnect()


    def on_disconnect(self, client, userdata, rc):
        print('Client Disconnected')
        
