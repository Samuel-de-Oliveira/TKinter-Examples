#-*-- Import area --*-#
from tkinter import * #
from colors import *  #
import os             #
#-*-----------------*-#

# If working in Windows the program will close.
if os.name in ('nt', 'dos'): print('Sorry, this software don\'t work in Windows :('); exit()

class mainWindow():
    def __init__(self):
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

    def run(self): 
        # The program basically work here  #
        # the "os.system" run a command in #
        # terminal and I have user the bash#
        # command to run the "runner.sh"   #
        # file. To know more about open the#
        # same file in directory.          #
        os.system(f'bash runner.sh {self.cmd.get()}')
        self.Win.destroy()

mainWindow()
print('\nBye, bye')
