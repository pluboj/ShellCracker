from tkinter import *


class App:

    def __init__(self, master):
        master.minsize(width=350, height=200)
        master.maxsize(width=350, height=200)
        master.configure(background='LightSalmon2')
        master.title('ShellCracker 1.0')

        search_img = PhotoImage(file="images/Search-Folder-icon.png")
        search_img = search_img.subsample(5)
        btn_search = Button(master, text="Select File")
        btn_search.config(image=search_img, width="240", height="80", border=2)
        btn_search.grid(row=0, column=1, sticky='e' + 'w', padx=50, pady=20)
        btn_search.image = search_img


root = Tk()
app = App(root)
root.mainloop()
