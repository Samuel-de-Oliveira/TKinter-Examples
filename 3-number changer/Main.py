from tkinter import *
from colors import *

class mainWindow():
    def __init__(self):
        self.Win = Tk()
        self.Win.resizable(False, False)
        self.Win.geometry('475x300')
        self.Win.title('Number Changer')
        self.Win['bg'] = color[0]
        
        self.number = 0

        # Widgets #
        Button(self.Win, text=' Plus 1 ', bg=color[2],
               font='arial 20 bold', command=self.plus).place(x=80, y='95')
        Button(self.Win, text='Minus 1', bg=color[2],
               font='arial 20 bold', command=self.minus).place(x=80, y='155')

        self.main = Label(self.Win, text=self.number,
                          bg=color[0], fg=color[3], font='arial 30 bold')

        self.main.place(x=280, y=110)

        self.Win.mainloop()

    def plus(self):
        self.number += 1
        print(self.number)
        self.main['text'] = self.number

    def minus(self):
        self.number -= 1
        if self.number < 0: self.number = 0

        print(self.number)
        self.main['text'] = self.number

mainWindow()
