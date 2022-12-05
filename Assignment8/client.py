# Import packages ZeroMQ, TIME, and JSON
import zmq
import time
import json
from tkinter import *
import os
import subprocess

#Tkinter page settings
ws = Tk()
ws.geometry('1200x900')
ws.title('Link')
f = ("Times bold", 14)

# Setup ZMQ and socket to talk to server on localhost 5555
context = zmq.Context()
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Set object ID
object_id = 1

#link
string = ""

#Communication pipeline settings. 
for request in range(1):
    # Send request
    print("Sending request %s …" % request)
    object_id = str(object_id)
    socket.send_string(object_id)
    print("Sent object [ %s ] …" % object_id)
    time.sleep(5)

    # Get the reply
    message = socket.recv_string()
    received_message = json.loads(message)
    print("Received reply %s [ %s ]" % (request, received_message))
    string = received_message['file_location']


#Tkinter GUI Settings

#Button Function- Return to main screen
def prevPage():
    ws.destroy()

#Link label 
Label(
    ws,
    text= string,
    padx=20,
    pady=20,
    #bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

#Button label
Button(
    ws, 
    text="Return to Main", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()