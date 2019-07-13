module.exports = async function (context, IoTHubMessages) {

    IoTHubMessages.forEach((message) => {
        context.log(message);
        context.bindings.signalRMessages = [{
            "target": "newMessage",
            "arguments": [message ]
        }];
    });
};