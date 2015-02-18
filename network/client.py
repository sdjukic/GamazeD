#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

connected = False
while not connected:

    resp = s.recv(1024)
    if resp == 'Welcome to GamazeD':
        connected = True
        print("Connection established")
        s.send("I am sending you map.")
    
    
s.close                     # Close the socket when done