from tkinter import *
from colors import  *

class window():
    def __init__(self) -> None:
        self.Win = Tk() # Main window object
        self.Win['bg'] = color[0] # Background
        self.Win.geometry('500x300') # Geometry
        self.Win.resizable(False, False) # Can't resize

        Button(text='Refresh', fg=color[3], bg=color[1], command=self.hello).place(x=222, y=260)
        self.Win.mainloop() # Main loop

    def hello(self): print("Hello, world!")

window()
