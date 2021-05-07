#python3.8
#import ax as ax
import paho.mqtt.client as mqtt
import time
import random

import numpy as np
import csv
from datetime import datetime
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd

from mpl_toolkits import mplot3d

client_id = f'python-mqtt-{random.randint(0, 100)}'
vibration = 0




def start_graph(fileName):
    plt.style.use('fivethirtyeight')

    x_values = []
    y_values = []

    index = count()
    file = pd.read_csv(fileName)
    headerList = ['Time', 'Vibration']
    fileName2 = fileName + "2"
    # converting data frame to csv
    print("adding headers")
    file.to_csv(fileName2, header=headerList, index=False)



def save_data(topic, vibration):
    print("writing to csv")
    currentTime = datetime.now(tz=None)
    dateStr = currentTime.strftime("%b %d %y")
    fileName = 'chewingDataWater'+dateStr+'.csv'
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        # adding header
        writer.writerow([currentTime, vibration, '',''])

    return

def save_data2(topic, flex):
    print("writing to csv")
    currentTime = datetime.now(tz=None)
    dateStr = currentTime.strftime("%b %d %y")
    fileName = 'chewingDataWater'+dateStr+'.csv'
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        # adding header
        writer.writerow([currentTime, '', flex,''])
    return

def save_data3(topic, distance):
    print("writing to csv")
    currentTime = datetime.now(tz=None)
    dateStr = currentTime.strftime("%b %d %y")
    fileName = 'chewingDataWater'+dateStr+'.csv'
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        # adding header
        writer.writerow([currentTime, '', '',distance])


def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    print(message.topic)
    topic = str(message.topic)

    if topic == "/python/arduino/mqtt/vibration":
        print("received message: ", str(message.payload.decode("utf-8")))
        vibration = str(message.payload.decode("utf-8"))
        save_data(topic, vibration)
        return vibration
    if topic == "/python/arduino/mqtt/flex":
        print("received message: ", str(message.payload.decode("utf-8")))
        flex = str(message.payload.decode("utf-8"))
        save_data2(topic, flex)
        return flex
    if topic == "/python/arduino/mqtt/distance":
        print("received message: ", str(message.payload.decode("utf-8")))
        print("received in the right topic")
        distance = str(message.payload.decode("utf-8"))
        save_data3(topic, distance)
        return distance


mqttBroker ="broker.emqx.io"
print("connecting to client")

client = mqtt.Client(client_id)
client.connect(mqttBroker)
print("connected to client ", client)
#create log to save data
currentTime = datetime.now(tz=None)
dateStr = currentTime.strftime("%b %d %y")
fileName = 'chewingDataWater' + dateStr + '.csv'
with open(fileName, 'a', newline='') as file:
    writer = csv.writer(file)
    # adding header
    writer.writerow(["Time", "Vibration", "Flex", "Distance"])

client.subscribe([("/python/arduino/mqtt/vibration",1),("/python/arduino/mqtt/flex",1),("/python/arduino/mqtt/distance",1)])
#client.subscribe("/python/arduino/mqtt/vibration")
client.on_message=on_message




client.loop_forever()
