from tkinter import *
import os
import subprocess

#Tkinter Initialization
ws = Tk()
ws.geometry('1200x900')
ws.title('FAQs')


f = ("Times bold", 14)

#Button Functions - Send Email
def nextPage():
    import email
    
#Button Function - Return to Main Screen
def prevPage():
    ws.destroy()
    os.system('python3 main_screen.py')
  
#FAQ main content label
Label(
    ws,
    text="This is a FAQ page",
    padx=20,
    pady=20,
    font=f
).pack(expand=True, fill=BOTH)

# Send Email Button
Button(
    ws, 
    text="More Questions? Send Email to Us!", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

#Return to main Button
Button(
    ws, 
    text="Return to Main", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()