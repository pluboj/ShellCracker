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
        # input_dir = Entry(master, width=60, bg="RosyBrown2")
        # input_dir.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)
        dir = Text(master, height=2, width=45, bg="RosyBrown2", state=DISABLED, relief="flat")
        dir.grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)
        search_img = PhotoImage(file="images/search_f.png")
        search_img = search_img.subsample(12)
        btn_search = Button(master, text="Select File")
        btn_search.config(image=search_img, width="40", height="40", border=0)
        btn_search.grid(row=0, column=10, sticky='e' + 'w', padx=10, pady=2)
        btn_search.image = search_img


root = Tk()
app = App(root)
root.mainloop()
