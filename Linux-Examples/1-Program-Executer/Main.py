from tkinter import *
from colors import *
import os

if os.name in ('nt', 'dos'): print('Sorry, this is not work in Windows :('); exit()

class mainWindow():
    def __init__(self):
        # Window style:
        Win = Tk()
        Win.resizable(False, False)
        Win.geometry('200x100')
        Win['bg'] = color[0]
        
        # widgets:
        Label(Win, text="Run an application here:", bg=color[0], fg=color[3]).pack() 
        cmd = Entry(Win, bg=color[2]).pack()
        Button(Win, bg=color[1], text='Run', command=Win.destroy).pack() 

        Win.mainloop()

mainWindow()
print('\nBye, bye')

