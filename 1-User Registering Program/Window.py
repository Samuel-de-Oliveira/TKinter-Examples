#-*---- import area ----*-#
from tkinter import *     #
from colors import color  #
import os                 #
#-*---------------------*-#

way = os.path.dirname(__file__)

# The Window
class mainWindow():
    def __init__(self):
        # Window style:
        self.Win = Tk() 
        self.Win.resizable(False, False) # Can't resize
        self.Win.geometry('320x190') # Geometry: 320 X 190
        self.Win.title('Register window') # Title
        self.Win['bg'] = color[0] # Background color

        #-- Creating widgets --#
        # Name entry: 
        self.lblName = Label(self.Win, text='Name:', bg=color[0], fg=color[3])
        self.Name = Entry(self.Win, bg=color[2], justify=CENTER, width=30)

        # Email entry:
        self.lblEmail = Label(self.Win, text='Email:', bg=color[0], fg=color[3])
        self.Email = Entry(self.Win, bg=color[2], justify=CENTER, width=30)

        # Password entry:
        self.lblPassw = Label(self.Win, text='Password:', bg=color[0], fg=color[3])
        self.Passw = Entry(self.Win, bg=color[2], justify=CENTER,
                           show='*', width=27)

        # Buttons:
        self.cancel = Button(self.Win, text='Cancel', bg=color[1],
                            command=lambda: self.Win.destroy())
        self.ok = Button(self.Win, text='Ok', bg=color[1],
                         command=self.winAlert)
        
        #-- Placing widgets --#
        self.lblName.place(x=0, y=25)
        self.Name.place(x=48, y=25)

        self.lblEmail.place(x=0, y=60)
        self.Email.place(x=48, y=60)

        self.lblPassw.place(x=0, y=95)
        self.Passw.place(x=72, y=95)

        self.ok.place(x=266,y=153)
        self.cancel.place(x=190, y=153)

        self.Win.mainloop() # The mainloop

    #-*--------------- Events and outhers windows ---------------*-#
    def winAlert(self):
        self.Alert = Tk()
        self.Alert.resizable(False, False) # Can't resize
        self.Alert.geometry('330x100') # Geometry: 330 X 100
        self.Alert['bg'] = color[0] # Background color
        self.Alert.title(f'{self.Name.get()} has registered successfully') # Title
        
        #-- Save the name in a .txt file with the user data --##
        with open(f'{way}/Users/{self.Name.get()}.txt', 'w+') as file:

            file.write(f'Username: {self.Name.get()}\n')
            file.write(f'Email:    {self.Email.get()}\n')
            file.write(f'Password: {self.Passw.get()}\n')

            print('User has been registered!') # Console message
        
        #-- Creating widgets --#
        self.showEmail = Label(self.Alert, text=f'His/Her Email: {self.Email.get()}',
                    bg=color[0], font='arial 10', fg=color[3])
        self.showPassw = Label(self.Alert, text=f'His/Her Password: {self.Passw.get()}',
                         bg=color[0], font='arial 10', fg=color[3])
        self.info = Label(self.Alert, text=f'check "Users/{self.Name.get()}.txt to see"',
                          font='Arial 10', bg=color[0], fg=color[3])
        self.close = Button(self.Alert, text='Close', bg=color[1],
                            command=lambda: self.Alert.destroy())
        
        #-- Placing widgets --#
        self.showEmail.pack()
        self.showPassw.pack()
        self.info.pack()
        self.close.pack(side=BOTTOM, pady=7)


        self.Alert.mainloop() #The mainloop

    #-*----------------------------------------------------------*-#
