from tkinter import *
from tkinter.ttk import *
from keygen import Keygen
import encrypt_decrypt as ed


def _insert_to_disabled_text(text_element, string):
    """Utility function that allows to insert text into a disabled tkinter Text widget"""
    text_element['state'] = NORMAL
    text_element.delete("1.0", END)
    text_element.insert(INSERT, string)
    text_element['state'] = DISABLED


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.key_gen = Keygen()
        self.master = master
        self.pack()
        self._create_widgets()
        self._set_keys()

    def _create_widgets(self):
        self.tab_control = Notebook(self)
        self.tab1 = GeneratedKeysFrame(self.tab_control)

        self.tab_control.add(self.tab1, text="Ключи, сгенерированные автоматически")
        # self.tab_control.add(self.tab2, text="Пользовательские ключи")
        self.tab_control.pack()

    def _set_keys(self):
        """Utility function for setting keys from keygen into the appropriate text fields"""
        _insert_to_disabled_text(self.tab1.open_key_text, str(self.key_gen.open_key))
        _insert_to_disabled_text(self.tab1.sequence_text, str(self.key_gen.seq))
        _insert_to_disabled_text(self.tab1.modulus_text, str(self.key_gen.modulus))
        _insert_to_disabled_text(self.tab1.multiplier_text, str(self.key_gen.multiplier))


class GeneratedKeysFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack
        self._create_widgets()

    def _create_widgets(self):
        self.open_key_label = Label(self, text="Открытый ключ")
        self.open_key_text = Text(self, height=1, state=DISABLED)
        self.open_key_label.pack()
        self.open_key_text.pack()

        self.sequence_label = Label(self, text="Последовательность(закрытый ключ)")
        self.sequence_text = Text(self, height=1, state=DISABLED)
        self.sequence_label.pack()
        self.sequence_text.pack()

        self.modulus_label = Label(self, text="Модуль(закрытый ключ)")
        self.modulus_text = Text(self, height=1, state=DISABLED)
        self.modulus_label.pack()
        self.modulus_text.pack()

        self.multiplier_label = Label(self, text="Множитель(закрытый ключ)")
        self.multiplier_text = Text(self, height=1, state=DISABLED)
        self.multiplier_label.pack()
        self.multiplier_text.pack()

        self.generate_btn = Button(self, text="Сгенерировать ключи")
        self.generate_btn.pack()


root = Tk()
root.title("Шифрователь-5000")
app = Application(root)
app.mainloop()

