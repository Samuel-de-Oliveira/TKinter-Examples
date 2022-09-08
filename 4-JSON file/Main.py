#-*------- import area -------*-#
from tkinter import *           #
from tkinter import messagebox  #
from colors import color        #
import json                     #
#-*---------------------------*-#

class mainWindow():
    def __init__(self) -> None:
        self.Win = Tk()
        self.Win.resizable(False, False) # Can't resize
        self.Win.geometry('540x120') # Geometry: 540 X 120
        self.Win.title('JSON file') # Title
        self.Win['bg'] = color[0] # Background color
        
        # Open the JSON file name "name.json" #
        with open('name.json', 'r') as file:
            self.nome = json.loads(file.read())

        # Create a automatic string #
        names = 'Names: '
        self.nome["names"].sort()
        for n, i in enumerate(self.nome["names"]):
            names += self.nome["names"][n]
            if self.nome["names"][n] != self.nome["names"][-1]: names += ', '
        
        # Print the string #
        Label(self.Win, text=names, bg=color[0], fg=color[3], font="arial 12").place(x=0, y=10)
        # Info Label #
        Label(self.Win, text="Check the name.json file to check names.",
              font="arial 8", fg=color[3], bg=color[0]).place(x=0, y=60)
        # Exit button #
        Button(self.Win, text="Exit", command=self.Win.destroy).place(x=489, y=90)

        # Window loop #
        self.Win.mainloop()

if __name__ == '__main__': mainWindow() # Start window
