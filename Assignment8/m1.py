import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8888")

while True:
    #  Indicate the communication on Terminal screen
    message = socket.recv()
    msg = str(message)
    print(f"Received request: {message}")

    # Wait for one second
    time.sleep(1)

    # Check if the message from image file upload
    if "IMAGEFILE" in msg:
        if "jpg" in msg or 'png' in msg or 'jpeg' in msg: 
        #  Send reply back to client
            socket.send_string("good")
        else:
            socket.send_string("bad")
    
    # Check if the message from text file upload
    elif "TEXTFILE" in msg:
        if "txt" in msg:
            socket.send_string("good")
        else:
            socket.send_string("bad")
