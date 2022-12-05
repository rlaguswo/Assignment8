import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import PIL
import os
import subprocess
from tkinter import filedialog
import zmq
import time
import json


#gloabal variables.

#Root for the UI
root = tk.Tk()
root.title("Image Memory Archive")
root.geometry('1200x900')

#Dividing Frames
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)
frame_drink = LabelFrame(root, text = "Record your memory. Note: When you make changes in your memo, you need to save the memo!")
frame_drink.pack(side="right", fill="both", expand=True)

#microservice pipelines

#Communication pipe for checking uploading invalid file format
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8888")

#Communication pipe for indicating the saving process on the main program. 
context_save = zmq.Context()
socket_save = context.socket(zmq.REQ)
socket_save.connect("tcp://localhost:9999")


#Layout for the GUI.
class Layout:
    
    #GUI buttons and labels setting Initialization 
    def __init__(self,master):

        self.master = master
        

        self.rootgeometry()
        
        #Initialize counter
        self.counter = 0

        # backgournd filename, label initialize
        self.background_image = None
        self.image_copy = None
        self.background = None
        self.filename = None
        self.textfile = None
        self.label = tk.Label(frame_burger)
        self.label.pack(fill='both', expand=True)
        self.img_counter = 0

        #Initialize text
        self.text = None
        #Image Upload Button
        self.button = Button(frame_burger, text='Upload or Replace Image File', command=self.loadbackground)
        self.button.pack(side = "bottom")
        
        #Memo Upload Button
        self.button2 = Button(frame_drink, text ='Upload Text file', command = self.loadmemo)
        self.button2.pack(side = "bottom")

        #Undo Image Button
        self.button3 = Button(frame_burger, text = 'Undo Image', command = self.clear_label_image)
        self.button3.pack(side = "bottom")
        
        #Undo Text Button
        self.button4 = Button(frame_drink, text = 'Undo the Writings', command = self.undo_text)
        self.button4.pack(side = "bottom")

        #Save Image Button
        self.button5 = Button(self.master, text = "Save Image", command = self.save_imag)
        self.button5.pack(side = "left")

        #Save Text Button
        self.button6 = Button(frame_drink, text = "Save Memo", command = self.save_txt)
        self.button6.pack(side = "left")

        #Move to FAQs Button
        self.button7 = Button(self.master, text= "FAQs", command = self.FAQ)
        self.button7.pack(side = "top")

        #Exit Button
        self.button8 = Button(self.master, text="Exit", command = self.exit_page)
        self.button8.pack(side="top")
       
       #GUI canvas initialize
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(fill=BOTH, expand=True)

     #size the root frame geometry
    def rootgeometry(self):
        x=int(self.master.winfo_screenwidth()*0.8)
        y=int(self.master.winfo_screenheight()*0.7)
        z = str(x) +'x'+str(y)
        self.master.geometry(z)

    #resize the image to fit in the frame
    def resizeimage(self,event):
        W = int(event.width * 0.9)
        image = self.image_copy.resize((event.width, event.height))
        self.image1 = ImageTk.PhotoImage(image)

    #clear the image in the label
    def clear_label_image(self):
        self.background= None
    
    #Undo the text content in the frame
    def undo_text(self):
        self.text.edit_undo()
    
   

    #Send memeo file and get status from microservice.
    def get_file_status(self, File):
        message = ""
            #Check send the file format to the microservice
        for request in range(1):
            print(f"Sending request {request} …")
            s = File
            socket.send_string(s)
            msg = socket.recv()
            message = str(msg)
            print(f"Received reply {request} [ {message} ]")
        return message

    
     #Load background of GUI
    def loadbackground(self):
        file = self.openfn()
        self.background_image = Image.open(file)
        self.image_copy = self.background_image.copy()
        self.background = ImageTk.PhotoImage(self.background_image.resize((self.canvas.winfo_width(), self.canvas.winfo_height())))
        self.label.configure(image=self.background)
        self.label.bind('<Configure>',self.resizeimage)

    #Load memo on the right frame of GUI
    def loadmemo(self):
        text_file = filedialog.askopenfilename()
        TF = "TEXTFILE"+str(text_file)
        while True:
            message = self.get_file_status(TF)
            
            #if status bad, upload the notification text file.
            if "bad" in message:
                text_file = 'wrong_text.txt'
            
            self.textfile = text_file

            if self.counter == 0:
                text_file = open(text_file, 'r')
            
            #Upload the selected text file on the right frame of GUI
            stuff = text_file.read()
            self.text = Text(frame_drink, undo= True)
            self.text.pack(side="right",expand=True, fill=BOTH)
            self.text.insert(END, stuff)
            text_file.close()
            self.counter = self.counter + 1
        

    #Check the file status before returning to load background
    def openfn(self):
        filename = filedialog.askopenfilename(title='open')
        F = "IMAGEFILE" + str(filename)
        while True:
            message = self.get_file_status(F)
            if"good" in message:
                self.filename = filename

            elif "bad" in message:
                filename = "wrong_image.png"
        
            return filename
    
    
    #Send the information what is going to be save to the microservice. 
    def send_save_status(self, string):
        message = ""
        for request in range(1):
            print(f"Sending request {request} …")
            s = string
            socket_save.send_string(s)
            msg = socket_save.recv()
            message = str(msg)
            print(f"Received reply {request} [ {message} ]")
        
        return message
   
    #Save image on FTP server, and demonstrates the process on the GUI
    def save_imag(self):
       picture = Image.open(self.filename) 
       os.remove("image.jpeg")
       picture = picture.save("image.jpeg", "JPEG")
       message = self.send_save_status("Image")

       root.title(message)
       os.system('python3 client.py')
       

    #Save the text, and demonstrates the process on GUI.
    def save_txt(self):
        message = self.send_save_status("Text")
        root.title(message)
        text = self.text
        os.remove('test.txt')
        text_file = open("/Users/hyunjaekim/Desktop/Class/Summer 2022/CS 361/Assignments/Assignment4/test.txt", "w")
        text_file.write(text.get(1.0, END))
        text_file.close()
        os.system('python3 client2.py')

        
    #Exit page from GUI.
    def exit_page(self):
        root.destroy()
        os.system("python3 exit.py")
    
    #Moves to FAQ from GUI.
    def FAQ(self):
        root.destroy()
        os.system('python3 FAQs.py')
       
#start the settings. 
a = Layout(root)
root.mainloop()


