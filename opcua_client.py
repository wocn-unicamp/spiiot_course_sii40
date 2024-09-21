# Import the OPC-UA client module
from opcua import Client

# Import the sleep function to add delays between iterations
from time import sleep

# Define the URL (endpoint) of the OPC-UA server
url = "opc.tcp://0.0.0.0:4840"

# Create an instance of the OPC-UA client, specifying the server's URL
client = Client(url)

# Connect the client to the server
client.connect()

# Print a message indicating that the client has successfully connected
print("OPC Client connected")

# Enter an infinite loop to continuously retrieve and print temperature and pressure values
while True:
    # Retrieve the node for the "Temperatura" variable from the server using its Node ID
    temp = client.get_node("ns=2;i=2")

    # Retrieve the node for the "Pressure" variable from the server using its Node ID
    press = client.get_node("ns=2;i=3")

    # Get the current value of the "Temperatura" variable from the server
    temperature = temp.get_value()

    # Get the current value of the "Pressure" variable from the server
    pressure = press.get_value()

    # Print the current temperature and pressure values
    print(temperature, pressure)

    # Pause execution for 2 seconds before fetching new values
    sleep(2)
