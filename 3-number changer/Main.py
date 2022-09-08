#-*-- Import area --*-#
from tkinter import * #
from colors import *  #
#-*-----------------*-#

class mainWindow():
    def __init__(self) -> None:
        # -- Window style -- #
        self.Win = Tk()
        self.Win.resizable(False, False)
        self.Win.geometry('475x300')
        self.Win.title('Number Changer')
        self.Win['bg'] = color[0]
        
        with open('number', "r") as file: self.number = file.read()

        # -- Widgets -- #
        Button(self.Win, text=' Plus 1 ', bg=color[2],
               font='arial 20 bold', command=self.plus).place(x=80, y='95')
        Button(self.Win, text='Minus 1', bg=color[2],
               font='arial 20 bold', command=self.minus).place(x=80, y='155')

        self.main = Label(self.Win, text=self.number,
                          bg=color[0], fg=color[3], font='arial 50 bold')
        self.main.place(x=300, y=110)

        self.Win.mainloop()

    def plus(self) -> None:
        #-*---------------------------------*-#
        #                                     #
        # When the "plus 1" button is pressed #
        # add +1 to the number variable and   #
        # change the label.                   #
        #                                     #
        #-*---------------------------------*-#
        self.number = int(self.number) + 1
        print(f'The number now is: {self.number}')
        with open('number', 'w') as file: file.write(str(self.number))
        self.main['text'] = self.number

    def minus(self) -> None:
        #-*---------------------------------*-#
        #                                     #
        # The same happens here, but this do  #
        # a -1                                #
        #                                     #
        #-*---------------------------------*-#
        self.number = int(self.number) - 1
        if self.number < 0: self.number = 0

        print(f'The number now is: {self.number}')
        with open('number', 'w') as file: file.write(str(self.number))
        self.main['text'] = self.number

mainWindow()
