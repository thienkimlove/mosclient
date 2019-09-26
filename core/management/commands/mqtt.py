
from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt
from core.models import Message


class Command(BaseCommand):
    help = 'Run Auto Cron'

    def handle(self, *args, **options):

        # The callback for when the client receives a CONNACK response from the server.
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))

            # Subscribing in on_connect() means that if we lose the connection and
            # reconnect then subscriptions will be renewed.
            client.subscribe("#")

        # The callback for when a PUBLISH message is received from the server.
        def on_message(client, userdata, msg):
            print(msg.topic + " and message " + str(msg.payload))

            Message.objects.create(topic=msg.topic, client_id="store_payload", message=msg.payload.decode('utf-8'))

        client = mqtt.Client("scoach", transport="websockets")
        client.username_pw_set(username="admin", password="tieungao")
        client.tls_set()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("mqtt.scoach.vn", 8083)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()



