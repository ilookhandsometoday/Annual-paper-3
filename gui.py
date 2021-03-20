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

        self.tab1.generate_btn.configure(command=self._generate_keys)

        self.tab_control.add(self.tab1, text="Ключи, сгенерированные автоматически")
        # self.tab_control.add(self.tab2, text="Пользовательские ключи")
        self.tab_control.pack()

    def _set_keys(self):
        """Utility function for setting keys from keygen into the appropriate text fields"""
        _insert_to_disabled_text(self.tab1.open_key_text, str(self.key_gen.open_key))
        _insert_to_disabled_text(self.tab1.sequence_text, str(self.key_gen.seq))
        _insert_to_disabled_text(self.tab1.modulus_text, str(self.key_gen.modulus))
        _insert_to_disabled_text(self.tab1.multiplier_text, str(self.key_gen.multiplier))

    def _generate_keys(self):
        self.key_gen = Keygen()
        self._set_keys()


class Subframe(Frame):
    """Abstract class created to reuse frame creation code. Should not be used by itself"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        pass


class GeneratedKeysFrame(Subframe):
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

        self.encrypt_frame = EncryptFrame(self)
        self.decrypt_frame = DecryptFrame(self)
        self.encrypt_frame.pack(side=LEFT)
        self.decrypt_frame.pack()


class EncryptFrame(Subframe):
    def _create_widgets(self):
        self.to_encrypt_label = Label(self, text="Текст для шифрования")
        self.to_encrypt_text = Text(self, height=3)
        self.to_encrypt_label.pack()
        self.to_encrypt_text.pack()

        self.encrypt_button = Button(self, text="Зашифровать", state=DISABLED)
        self.encrypt_button.pack()

        self.encrypted_label = Label(self, text="Зашифрованный текст")
        self.encrypted_text = Text(self, height=3, state=DISABLED)
        self.encrypted_label.pack()
        self.encrypted_text.pack()


class DecryptFrame(Subframe):
    def _create_widgets(self):
        self.to_decrypt_label = Label(self, text="Текст для расшифровки")
        self.to_decrypt_text = Text(self, height=3)
        self.to_decrypt_label.pack()
        self.to_decrypt_text.pack()

        self.decrypt_button = Button(self, text="Расшифровать", state=DISABLED)
        self.decrypt_button.pack()

        self.decrypted_label = Label(self, text="Расшифрованный текст")
        self.decrypted_text = Text(self, height=3, state=DISABLED)
        self.decrypted_label.pack()
        self.decrypted_text.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Шифрователь-5000")
    app = Application(root)
    app.mainloop()

