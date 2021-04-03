from datetime import datetime, time
import time
import json

import paho
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import paho.mqtt.client as mqtt


def view(request):
    
    z = request.POST.dict()
    today = datetime.now()
    d1 = today.strftime("%d-%m-%Y %H:%M:%S")
    z["timestamp"] = d1
    x = json.dumps(z)
    fin = json.loads(x)
    final(x)
    
    # broker = z["host"]
    # topic = z["topic"]
    # port = z["port"]
    # loop(broker, topic, port)
    return render(request, "index.html",{
        "z": z
})

#
# def on_message(client, userdata, message):
#     topic = "data/ppmp"
#     sub_msg = str((message.payload.decode("utf-8")))
#     print("received message =", sub_msg)
#     time.sleep(1)
#     jsonData = json.loads(sub_msg)
#     print(jsonData)
#     # print(jsonData["measurements"][0]["series"]["TempC"][0])
#     client.publish(topic, sub_msg)  # publish
#
#
# def loop(broker, topic, port):
#     client = mqtt.Client()
#     client.on_message = on_message
#     client.connect(broker)  # connect
#     client.subscribe(topic)  # subscribe
#     time.sleep(2)
#     client.loop_forever()  # stop loop


def final(obj):
    mqttc = mqtt.Client("jacob-clientid")
    host = "broker.mqttdashboard.com"
    port = 1883
    keepalive = 60
    mqttc.connect(host, port, keepalive)
    mqttc.loop_start()
    msg = obj
    print(msg)
    topic = "Siqsess_IoT/message"

    mqttc.publish(topic, msg, qos=2)

    mqttc.loop_stop()
