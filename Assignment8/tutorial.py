from tkinter import *
import os
import sys
import subprocess
ws = Tk()
ws.geometry('1200x900')
ws.title('PythonGuides')

v = StringVar()


f = ("Times bold", 16)

def prevPage():
    ws.destroy()
    os.system('python3 main_screen.py')


#Instruction labels intialization
label1 = Label(ws, font= f)
label3 = Label(ws, font=f)
label4 = Label(ws, font=f)
label5 = Label(ws, font=f)
label6 = Label(ws, font=f)
label7 = Label(ws, font=f)

# Instruction content
label1['text'] = 'Welcome to Image Memory Archive Instructions.'
label3['text'] = 'If you press Upload Image Button, you need to manually find the jpeg or png file from your local computer.'
label4['text'] = 'If you press Upload Memo Button, you need to manually find txt file from your local computer'
label5['text'] = 'When you press Save Image Button, the program will save the image in FTP Server.'
label6['text'] = 'When you press Save Memo Button, the program will save the memo in FTP Server'
label7['text'] = 'When you press Undo Button, the program will undo your work in the program. Note that you need to save the changes for the Memo.'

#Placing Instruction content in the GUI.
label1.pack(expand=True,fill=BOTH)
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()

# Go to main program Button
Button(
    ws, 
    text="Go to Main", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side="bottom")

ws.mainloop()