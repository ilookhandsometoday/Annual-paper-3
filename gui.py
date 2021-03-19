from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        self.tab_control = Notebook(self)
        self.tab1 = Frame(self.tab_control)
        self.tab2 = Frame(self.tab_control)

        self.tab_control.add(self.tab1, text="Ключи, сгенерированные автоматически")
        self.tab_control.add(self.tab2, text="Пользовательские ключи")
        self.tab_control.pack()


root = Tk()
root.title("Шифрователь-5000")
app = Application(root)
app.mainloop()

