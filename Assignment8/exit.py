from tkinter import *
import os
import subprocess

#Tkinter Initialization
ws = Tk()
ws.geometry('400x300')
ws.title('Exit Page')


f = ("Times bold", 14)

#Button Functions -Quit
def nextPage():
    ws.destroy()
    
#Button Function - Return to Main
def prevPage():
    ws.destroy()
    os.system('python3 main_screen.py')

#Exit page main contents
Label(
    ws,
    text="Are you Sure to Exit?",
    padx=20,
    pady=20,
    font=f
).pack( fill=BOTH)

Label(
    ws,
    text="It will close the entire work which you did. ",
    padx=20,
    pady=20,
    font=f
).pack(fill=BOTH)

Label(
    ws,
    text="Is this really what you want to do?",
    padx=20,
    pady=20,
    font=f
).pack(fill=BOTH)


# Select Buttons

# Quit  Button
Button(
    ws, 
    text="Yes", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

# Return to Main software Button
Button(
    ws, 
    text="No", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()