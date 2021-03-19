from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def create_widgets(self):
        pass


root = Tk()
root.title("Шифрователь-5000")
app = Application(root)
app.mainloop()

