from tkinter import *


class App:
    def __init__(self, master):
        master.minsize(width=520, height=100)
        master.maxsize(width=520, height=100)
        master.title('ShellCracker 1.0')


root = Tk()
app = App(root)
root.mainloop()