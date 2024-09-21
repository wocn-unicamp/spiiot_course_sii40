# Mini-Course: Standards and Protocols for Industry 4.0​

Course: <a href="https://sii40.ing.unibo.it/"> Services and Innovation for Industry 4.0 </a>

This repository contains two Python scripts:

- **Server Script**: Simulates an OPC-UA server that provides two variables, temperature and pressure, with random values.
- **Client Script**: Connects to the OPC-UA server and retrieves the temperature and pressure values periodically.

## Prerequisites

Before running the server and client scripts, ensure you have the following installed on your machine:

1. **Python**: This project requires Python 3.6 or higher. You can download Python [here](https://www.python.org/downloads/).

2. **Required Libraries**:
   - **`opcua`**: This library allows you to create and interact with OPC-UA servers and clients.
   - **`random`**: Used to generate random numbers (for server simulation).
   - **`time`**: Used for adding delays between data fetches on the client side.

## Installing Required Libraries

To install the necessary Python libraries, follow these steps:

1. **Install `pip`**: If you don't have `pip` installed (the Python package manager), you can install it by following [these instructions](https://pip.pypa.io/en/stable/installation/).

2. **Install the `opcua` library**:  
   You can install the OPC-UA library using `pip` by running the following command in your terminal or command prompt:

   ```bash
   pip install opcua
   ```

3. **(Optional) Create a Virtual Environment**:
   It is recommended to use a virtual environment to manage dependencies. You can create and activate one using the following commands:

   ```bash
   # Create a virtual environment
   python -m venv opcua-env

   # Activate the virtual environment (Windows)
   opcua-env\Scripts\activate

   # Activate the virtual environment (Mac/Linux)
   source opcua-env/bin/activate
   ```

4. **Install Dependencies**:  
   If using a virtual environment, install the required dependencies inside the environment by running:

   ```bash
   pip install opcua
   ```

---

## Running the Server Script

The **server script** simulates an OPC-UA server that generates random temperature and pressure values.

### Steps to Execute:

1. **Open a terminal/command prompt**.

2. **Navigate to the folder containing the server script** (replace `<path_to_folder>` with the actual path to your folder):

   ```bash
   cd <path_to_folder>
   ```

3. **Run the server script**:

   ```bash
   python server_script.py
   ```

   If the script runs successfully, you will see the message:

   ```text
   Server started at opc.tcp://0.0.0.0:4840
   ```

   The server will now be running and continuously updating the temperature and pressure values.

---

## Running the Client Script

The **client script** connects to the OPC-UA server and retrieves the temperature and pressure values, printing them every 2 seconds.

### Steps to Execute:

1. **Open another terminal/command prompt**.

2. **Navigate to the folder containing the client script** (replace `<path_to_folder>` with the actual path to your folder):

   ```bash
   cd <path_to_folder>
   ```

3. **Run the client script**:

   ```bash
   python client_script.py
   ```

   If the client connects successfully, you will see a message like this:

   ```text
   OPC Client connected
   ```

   Then, the script will start printing the retrieved temperature and pressure values:

   ```text
   25 550
   30 670
   12 890
   ```

   The client will continue retrieving and printing values every 2 seconds.

---

## Summary of Commands

### Install Required Libraries:

```bash
pip install opcua
```

### Running the Server:

```bash
python server_script.py
```

### Running the Client:

```bash
python client_script.py
```

---

## Notes

- Make sure to run the **server script** before the **client script**, as the client needs the server to be running to retrieve data.
- Both the server and client use the same endpoint (`opc.tcp://0.0.0.0:4840`). You can modify the IP address and port if necessary, but remember to update both scripts to reflect the change.

---

Feel free to reach out if you encounter any issues or need further assistance!

Code made by: Eduardo Mosca <br>
Contact: e242678@dac.unicamp.br
