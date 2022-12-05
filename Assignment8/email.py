from tkinter import *
import os
import sys
import subprocess
ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')


f = ("Times bold", 14)
def nextPage():
    ws.destroy()
   
   
# Email notification
Label(
    ws,
    text="Email has been sent!",
    padx=20,
    pady=20,
   
    font=f
).pack(expand=True, fill=BOTH)

#Email Close Button
Button(
    ws, 
    text="Close", 
    font=f,
    command=nextPage
    ).pack( expand=TRUE, side='bottom')



ws.mainloop()
