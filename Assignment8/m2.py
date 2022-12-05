import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9999")


while True:
    #  Indicate the communication on Terminal screen
    message = socket.recv()
    msg = str(message)
    print(f"Received request: {message}")

    #  Wait for one second
    time.sleep(1)

    #Check if the message from image save button
    if "Image" in msg:
        socket.send_string("Image Saved in FTP Server!")
    
    #Check if the message from text save button
    if "Text" in msg:
    #  Send reply back to client
        socket.send_string("Text Saved!")