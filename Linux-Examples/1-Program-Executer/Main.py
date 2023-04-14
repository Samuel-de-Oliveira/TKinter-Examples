#-*------- Import area -------*-#
from tkinter import *           #
from tkinter import messagebox  #
from colors import *            #
import os                       #
#-*---------------------------*-#

# If working in Windows or Mac the program will close.
if os.name in ('nt', 'dos', 'win32', 'cygwin', 'darwin'):
    messagebox.showerror('Error: Sorry, this software doesn\'t work in Windows!')
    exit()


class mainWindow():
    def __init__(self) -> None:
        #- Window style -#
        self.Win = Tk() # The window
        self.Win.resizable(False, False) # Can't resize
        self.Win.geometry('200x100') # Geometry
        self.Win['bg'] = color[0] # Background
        
        #- widgets -#
        Label(self.Win, text="Run an application here:", bg=color[0], fg=color[3]).pack() # Label
        
        # Entry: 
        self.cmd = Entry(self.Win, bg=color[2])
        self.cmd.pack()

        Button(self.Win, bg=color[1], text='Run', command=self.run).pack() # Button

        self.Win.mainloop() # The mainloop

    def run(self) -> None: 
        # Run the command and then Close #
        # the software. It's very simple #
        # anyway.                        #
        os.system(f'{self.cmd.get()} &')
        self.Win.destroy()

mainWindow()
print('\nBye, bye')
