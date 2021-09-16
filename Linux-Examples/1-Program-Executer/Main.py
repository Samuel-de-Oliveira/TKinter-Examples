from tkinter import *
from colors import *

class mainWindow():
    def __init__(self):
        # Window style:
        Win = Tk()
        Win.resizable(False, False)
        Win.geometry('500x500')
        Win['bg'] = color[0]
        
        # widgets:
        Label(Win, text="Run an application here:", bg=color[0], fg=color[3]).place(x=0, y=0)
        cmd = Entry(Win, bg=color[2]).pack()
        Button(Win, bg=color[1], text='Run').place(x=10, y=100)

        Win.mainloop()

mainWindow()
print('\nBye, bye')

