#-*------- import area -------*-#
from tkinter import *           #
from tkinter import messagebox  #
import os                       #
from colors import color        #
#-*---------------------------*-#

way = os.path.dirname(__file__) # this take the directory where are the tkinter template

#-*------------------------------------------*-#
# To add more arguments you need to edit       #
# somethings in this file:                     #
#                                              #
# * The window geometry                        #
# * add a label and an entry in window with    #
#   35px(Y) of space                           #
#                                              #
# Following this you can add more things       #
# without lost the format of formulary         #
#-*------------------------------------------*-#

# The Window
class mainWindow():
    def __init__(self) -> None:
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
                            command=self.Win.destroy)
        self.ok = Button(self.Win, text='Ok', bg=color[1],
                         command=self.registering)
        
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

    #-- Events and outhers windows --#
    def registering(self) -> None:
        if len(self.Name.get()) == 0 or len(self.Email.get()) == 0 or len(self.Passw.get()) == 0:
            
            # If one of entries have nothing writed: show a error message.
            messagebox.showerror("Error: Missing arguments",
            "Check if you are not forgetting anything")

        else: # else create a window
            self.Alert = Tk()
            self.Alert.resizable(False, False) # Can't resize
            self.Alert.geometry('335x110') # Geometry: 335 X 110
            self.Alert['bg'] = color[0] # Background color

            # The titlle show the user's name:
            self.Alert.title(f'{self.Name.get()} has registered successfully')

            #-- Save the name in a .txt file with the user data --##
            with open(f'{way}/Users/{self.Name.get()}.txt', 'w+') as file:

                file.write(f'Username: {self.Name.get()}\n') # His/Her Username
                file.write(f'Email:    {self.Email.get()}\n') # His/Her Email
                file.write(f'Password: {self.Passw.get()}\n') # HIs/Her Password

                print('User has been registered!') # Console message
            
            #-- Creating widgets --#
            # The widgets will show the Email and Password only,
            # the username is in the title
            self.showEmail = Label(self.Alert, text=f'His/Her Email: {self.Email.get()}',
                        bg=color[0], font='arial 10', fg=color[3])
            self.showPassw = Label(self.Alert, text=f'His/Her Password: {self.Passw.get()}',
                            bg=color[0], font='arial 10', fg=color[3])
            self.info = Label(self.Alert, text=f'check "Users/{self.Name.get()}.txt to see"',
                            font='Arial 10', bg=color[0], fg=color[3])
            self.close = Button(self.Alert, text='Close', bg=color[1],
                                command=self.Alert.destroy)
            
            #-- Placing widgets --#
            self.showEmail.pack()
            self.showPassw.pack()
            self.info.pack()
            self.close.pack(side=BOTTOM, pady=7)

            self.Alert.mainloop() #The mainloop
