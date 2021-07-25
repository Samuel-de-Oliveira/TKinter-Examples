#-*---- The imports ----*-#
from tkinter import *     #
from colors import color  #
#-*---------------------*-#

# Window Config
class mainWindow():
    def __init__(self) -> None:
        self.Win = Tk()
        self.Win.resizable(False, False) # can't resize
        self.Win.geometry('680x310') # Geometry: 680 X 310
        self.Win.title('Bottom info') # Title
        self.Win['bg'] = color[1] # Background color
        self.Win.bind('<Key>', lambda i: self.theBar(i)) # Bind to read keyboard
        self.numKeyPress = 0 # A var to show the number of keys presseds

        #-- Creating widgets --#
        #-- Here is the bar! --#
        self.infoBar = Label(self.Win,
                             # Bar formating 
                             bg=color[0], font='arial 9', anchor=W, fg=color[2],

                             #-*-----------------------------------------------*-#
                             # To add things to the bar you need to make a edit  #
                             # like this down in the text var.                   #
                             # To add the funcionalities go to events down and   #
                             # found "theBar" event.                             #
                             #-*-----------------------------------------------*-#

                             text='Last key pressed: None   |'+
                                 f'   Times pressed: {self.numKeyPress}   |'+
                                  '   Dividers of nothing: Nothing')

        self.divLabel = Label(self.Win, fg=color[2], bg=color[0], font='arial',
                              text='Digit a number: ')
        self.numGet = Entry(self.Win, bg=color[3])
        

        #-- Placing Widgets --#
        self.divLabel.place(x=0, y=140)
        self.numGet.place(x=120, y=140)
        self.infoBar.pack(side=BOTTOM, fill=X)

        self.Win.mainloop() # The mainloop

    #-- Events and outhers windows --#
    def theBar(self, key) -> None:
        #-*---------------------------------------------------------*-#
        # Here is the bar config, you need to change this to modify   #
        # or add something into                                       #
        #-*---------------------------------------------------------*-#
        
        self.numKeyPress += 1 # Number of key pressed add 1

        # If in entry have something:
        if len(self.numGet.get()) > 0:
            # try give the txt some infos
            try:
                txt = (f'Last key pressed: {key.keysym}   |'+
                       f'   Times pressed: {self.numKeyPress}   |'+
                       f'   Dividers of {self.numGet.get()}: {self.dividers(self.numGet.get())}')

            # If have any error (like typeError) give outher infos
            except: 
                txt = (f'Last key pressed: {key.keysym}   |'+
                       f'   Times pressed: {self.numKeyPress}   |'+
                       f'   Dividers of Nothing: Nothing')
        else:
            txt = (f'Last key pressed: {key.keysym}   |'+
                   f'   Times pressed: {self.numKeyPress}   |'+
                   f'   Dividers of Nothing: Nothing')
        
        self.infoBar['text'] = txt # And finally give the bar the infos

    def dividers(self, num) -> list:
        # Here return the dividers
        divs = []
        for n in range(1, int(num)+1):
            if int(num) % n == 0:
                divs.append(n)
        return divs
