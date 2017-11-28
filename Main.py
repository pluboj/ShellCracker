from tkinter import *


class App:

    def __init__(self, master):
        master.minsize(width=350, height=200)
        master.maxsize(width=350, height=200)
        master.configure(background='LightSalmon2')
        master.title('ShellCracker 1.0')

        # Menubar
        menu_bar = Menu(master)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", accelerator="Alt + F4",
                              command=self.turn_off)
        view_menu = Menu(menu_bar, tearoff=0)
        about_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='File', menu=file_menu)
        menu_bar.add_cascade(label='View', menu=view_menu)
        menu_bar.add_cascade(label='About', menu=about_menu)
        master.config(menu=menu_bar)

        # File chooser button
        search_img = PhotoImage(file="images/Search-Folder-icon.png")
        search_img = search_img.subsample(5)
        btn_search = Button(master, text="Select File")
        btn_search.config(image=search_img, width="240", height="80", border=2, cursor='hand2')
        btn_search.grid(row=0, column=1, sticky='e' + 'w', padx=50, pady=20)
        btn_search.image = search_img

    def turn_off(self):
        root.destroy()


root = Tk()
app = App(root)
root.mainloop()
