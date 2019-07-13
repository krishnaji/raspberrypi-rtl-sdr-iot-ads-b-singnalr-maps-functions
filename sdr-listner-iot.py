#!/usr/bin/python
#https://github.com/Azure-Samples/azure-iot-samples-python/blob/master/iot-hub/Quickstarts/simulated-device-2/SimulatedDevice.py

import select
import socket
import sys
import time
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue
CONNECTION_STRING = "HostName=adsb.azure-devices.net;DeviceId=rtl-sdr;SharedAccessKey="
PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 10000
MSG_TXT = "{\"icao\": \"%s\",\"alt\": %s,\"lat\": %s,\"lon\": %s }"
def send_confirmation_callback(message, result, user_context):
    print ( "IoT Hub responded to message with status: %s" % (result) )

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client

client = iothub_client_init()

while True:
  try:
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.connect(('localhost',30003))
    socketServer.settimeout(30)
    message = (socketServer.recv(512)).split(',')
#    print(message)
    if(message[1]=='3' ):
        print (message)
        ICAO,ALT,LAT,LON=message[4], message[11],message[14],message[15]
        msg_txt_formatted = MSG_TXT % (ICAO,ALT,LAT,LON)
        event = IoTHubMessage(msg_txt_formatted)
        print( "Sending message: %s" % event.get_string() )
        client.send_event_async(event,send_confirmation_callback,None)

  except socket.error as e:
    err = e.args[0]
    print(err)