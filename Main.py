from tkinter import *


class App:
    input_dir = None

    def __init__(self, master):
        master.minsize(width=520, height=100)
        master.maxsize(width=520, height=100)
        master.configure(background='LightSalmon2')
        master.title('ShellCracker 1.0')

        Label(master, text="Directory:", bg="LightSalmon2", font=("Helvetica", 12))\
            .grid(row=0, column=0, sticky='e', pady=20)
        global input_dir
        input_dir = Entry(master, width=60, bg="RosyBrown2")
        input_dir.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)


root = Tk()
app = App(root)
root.mainloop()
