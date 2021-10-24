from tkinter import *

class mainWindow():
    def __init__(self):
        self.Win = Tk()
        self.Win.resizable(False, False)
        self.Win.geometry('500x300')

        # Widgets #
        Button(self.Win, text='Olá, mundo!').pack()

        self.Win.mainloop()

mainWindow()
