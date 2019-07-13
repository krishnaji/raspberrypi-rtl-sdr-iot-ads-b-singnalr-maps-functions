

![](https://raw.githubusercontent.com/krishnaji/raspberrypi-rtl-sdr-iot-ads-b-singnalr-maps-functions/master/RealtimeFlightMap.gif)

### Hadware 
- Raspberry Pi
- RTL SDR Receiver & Antenna

    ![](https://raw.githubusercontent.com/krishnaji/raspberrypi-rtl-sdr-iot-ads-b-singnalr-maps-functions/master/setup.jpg)

### RTL-SDR and Mode S decoder Setup
Plugin your rtl-sdr into your raspberry-pi. Build and run the docker image on your raspberry pi.
 
```docker build -t  dump1090 -f Dockerfile.arm32v7 .```

```docker run -d --name dump1090 --privileged -v /dev/bus/usb:/dev/bus/usb -p 8080:8080 -p 30003:30003 --restart always dump1090:latest```

### IoT Hub and Device Setup
Follow [this](https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python) guide to setup IoT Hub and register your device.

Execute following on your raspberry pi ```python sdr-listner-iot.py```. This listens to port 30003 and then sends the SBS Basestation messages to Azure IoT hub.

### Azure Functions 
This application uses [IoT Hub ](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-iot) trigger and [SignalR](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-signalr-service) output bindings to send realtime data to Azure Maps. 
Start the functions app with ``` func host start ```
 
### Azure Maps 
Get your maps subscription key from [here]() and update ```maps.html```. Open maps.html to watch the flights on maps.




