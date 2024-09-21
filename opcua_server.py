# Import the OPC-UA server module
from opcua import Server

# Import the randint function to generate random numbers
from random import randint

# Create an instance of the OPC-UA server
server = Server()

# Define the endpoint URL for the server (listening on all interfaces on port 4840 which is the default port for protocol)
url = "opc.tcp://0.0.0.0:4840"

# Set the server's endpoint to the specified URL
server.set_endpoint(url)

# Define a custom namespace called "simmulator"
name_space = "simmulator"

# Register the namespace and store the returned unique index
add_space = server.register_namespace(name_space)

# Get the root 'Objects' node where we will add our custom objects and variables
node = server.get_objects_node()

# Add an object named "Parameters" to the Objects node under the specified namespace
param = node.add_object(add_space, "Parameters")

# Add a variable "Temperature" to the "Parameters" object, initializing it to 0
temp = param.add_variable(add_space, "Temperatura", 0)

# Add a variable "Pressure" to the "Parameters" object, initializing it to 0
press = param.add_variable(add_space, "Pressure", 0)

# Set the "Temperature" variable to be writable
temp.set_writable()

# Set the "Pressure" variable to be writable
press.set_writable()

# Start the OPC-UA server so it can accept client connections
server.start()

# Print a message indicating the server has started with the server's endpoint URL
print(f"Server started at {url}")

# Enter an infinite loop where temperature and pressure values are continuously updated
while True:
    # Generate a random temperature value between 10 and 50
    temperature = randint(10, 50)

    # Generate a random pressure value between 200 and 999
    pressure = randint(200, 999)

    # Update the value of the "Temperatura" variable with the new temperature
    temp.set_value(temperature)

    # Update the value of the "Pressure" variable with the new pressure
    press.set_value(pressure)
