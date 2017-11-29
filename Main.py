from tkinter import *
import tkinter.filedialog
from tkinter.ttk import Progressbar
import time
import threading
from FileProcessor import FileProcessor


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
        about_menu.add_command(label="About")
        about_menu.add_command(label="Help")
        menu_bar.add_cascade(label='File', menu=file_menu)
        menu_bar.add_cascade(label='View', menu=view_menu)
        menu_bar.add_cascade(label='About', menu=about_menu)
        master.config(menu=menu_bar)

        # File chooser button
        search_img = PhotoImage(file="images/Search-Folder-icon.png")
        search_img = search_img.subsample(5)
        self.btn_search = Button(master, text="Select File", command=self.process_file)
        self.btn_search.config(image=search_img, width="240", height="80", border=2,
                               cursor='hand2', bg='lightblue')
        self.btn_search.grid(row=0, column=1, sticky='e' + 'w', padx=50, pady=20)
        self.btn_search.image = search_img

        # Progressbar
        self.progress = Progressbar(master, orient=HORIZONTAL, length=245, mode='indeterminate')

    def process_file(self):

        def progress():
            self.progress.grid(row=1, column=1, sticky='e', padx=50)
            self.progress.start()
            time.sleep(5)
            self.progress.stop()
            self.progress.grid_forget()
            self.btn_search['state'] = 'normal'

        file = tkinter.filedialog.askopenfilename(filetypes=[("MS Excel", "*.xlsx")])
        if file:
            p = FileProcessor(file)
            p.process()
            self.btn_search['state'] = 'disabled'
            threading.Thread(target=progress).start()

    @staticmethod
    def turn_off():
        root.destroy()


root = Tk()
app = App(root)
root.mainloop()
