import tkinter.messagebox as mb
from tkinter import *
from tkinter.ttk import *
import ast
from keygen import Keygen
import encrypt_decrypt as ed

_WRONG_FORMAT_ERROR_MESSAGE = "Неверный формат текста для расшифровки.\n" + \
                              "[c1, c2, c3,...,ci],\n" + \
                              "где ci - это целое число.\n"


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
        # tab1
        self.tab1 = GeneratedKeysFrame(self.tab_control)

        self.tab1.generate_btn.configure(command=self._generate_keys)

        self.tab1.encrypt_frame.to_encrypt_text.bind("<KeyRelease>", Application._on_to_encrypt_key_released)
        self.tab1.decrypt_frame.to_decrypt_text.bind("<KeyRelease>", Application._on_to_decrypt_key_released)

        self.tab1.encrypt_frame.encrypt_button.configure(command=self._on_encrypt_button_tab1)
        self.tab1.decrypt_frame.decrypt_button.configure(command=self._on_decrypt_button_tab1)

        # tab2
        self.tab2 = UserKeysFrame(self.tab_control)

        self.tab2.encrypt_frame.to_encrypt_text.bind("<KeyRelease>", Application._on_to_encrypt_key_released)
        self.tab2.decrypt_frame.to_decrypt_text.bind("<KeyRelease>", Application._on_to_decrypt_key_released)

        self.tab2.encrypt_frame.encrypt_button.configure(command=self._on_encrypt_button_tab2)

        self.tab_control.add(self.tab1, text="Ключи, сгенерированные автоматически")
        self.tab_control.add(self.tab2, text="Пользовательские ключи")
        self.tab_control.pack()

    def _set_keys(self):
        """Utility function for setting keys from keygen into the appropriate text fields"""
        _insert_to_disabled_text(self.tab1.open_key_text, str(self.key_gen.open_key))
        _insert_to_disabled_text(self.tab1.sequence_text, str(self.key_gen.seq))
        _insert_to_disabled_text(self.tab1.modulus_text, str(self.key_gen.modulus))
        _insert_to_disabled_text(self.tab1.multiplier_text, str(self.key_gen.multiplier))

    def _generate_keys(self):
        """Function to generate keys and insert them into the appropriate text fields"""
        self.key_gen = Keygen()
        self._set_keys()

    @classmethod
    def _on_to_encrypt_key_released(cls, event):
        widget = event.widget
        if widget.get("1.0", END).rstrip():
            widget.master.encrypt_button['state'] = NORMAL
        else:
            widget.master.encrypt_button['state'] = DISABLED

    @classmethod
    def _on_to_decrypt_key_released(cls, event):
        widget = event.widget
        if widget.get("1.0", END).rstrip():
            widget.master.decrypt_button['state'] = NORMAL
        else:
            widget.master.decrypt_button['state'] = DISABLED

    def _on_encrypt_button_tab1(self):
        text = self.tab1.encrypt_frame.to_encrypt_text.get("1.0", END)
        encrypted_text = ed.encrypt(text, self.key_gen)
        _insert_to_disabled_text(self.tab1.encrypt_frame.encrypted_text, str(encrypted_text))

    def _on_decrypt_button_tab1(self):
        try:
            encrypted_text = ast.literal_eval(self.tab1.decrypt_frame.to_decrypt_text.get("1.0", END))
            text = ed.decrypt(encrypted_text, self.key_gen)
        except UnicodeDecodeError:
            mb.showerror(title="Ошибка", message="Зашифрованные данные нельзя расшифровать\n" +
                                                 "предложенным закрытым ключом")
        except (ValueError, SyntaxError):
            mb.showerror(title="Ошибка", message=_WRONG_FORMAT_ERROR_MESSAGE)
        except OverflowError:
            mb.showerror(title="Ошибка", message=(_WRONG_FORMAT_ERROR_MESSAGE +
                                                  "Один из элементов предложенной последовательности - не число"))
        else:
            _insert_to_disabled_text(self.tab1.decrypt_frame.decrypted_text, text)

    def _on_encrypt_button_tab2(self):
        open_key_entry = self.tab2.open_key_text.get().strip()
        if open_key_entry:
            try:
                open_key = ast.literal_eval(open_key_entry)
            except SyntaxError:
                mb.showerror("Ошибка", _WRONG_FORMAT_ERROR_MESSAGE)
            else:
                if isinstance(open_key, list) and all(isinstance(element, int) for element in open_key):
                    text = self.tab2.encrypt_frame.to_encrypt_text.get("1.0", END)
                    encrypted_text = ed.encrypt(text, self.key_gen, open_key)
                    _insert_to_disabled_text(self.tab2.encrypt_frame.encrypted_text, str(encrypted_text))
                else:
                    mb.showerror("Ошибка", _WRONG_FORMAT_ERROR_MESSAGE +
                                 "Один из элементов списка не число\n" +
                                 "или на вход подан не список.")
        else:
            mb.showerror("Ошибка", "Открытый ключ не задан!")


class Subframe(Frame):
    """Abstract class created to reuse frame creation code. Should not be used by itself"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self._create_widgets()

    def _create_widgets(self):
        raise NotImplementedError


class GeneratedKeysFrame(Subframe):
    """Layout for the generated keys tab"""

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


class UserKeysFrame(Subframe):
    """Layout for the user keys tab"""

    def _create_widgets(self):
        self.warning_label = Label(self, text="Внимание! Ключи для этой вкладки настоятельно "
                                              "рекомендуется копировать из первой вкладки "
                                              "копии этого приложения."
                                              "Формат ключей аналогичен формату ключей на первой вкладке")
        self.warning_label.pack()

        self.open_key_label = Label(self, text="Открытый ключ")
        self.open_key_text = Entry(self)
        self.open_key_label.pack()
        self.open_key_text.pack()

        self.sequence_label = Label(self, text="Последовательность(закрытый ключ)")
        self.sequence_text = Entry(self)
        self.sequence_label.pack()
        self.sequence_text.pack()

        self.modulus_label = Label(self, text="Модуль(закрытый ключ)")
        self.modulus_text = Entry(self)
        self.modulus_label.pack()
        self.modulus_text.pack()

        self.multiplier_label = Label(self, text="Множитель(закрытый ключ)")
        self.multiplier_text = Entry(self)
        self.multiplier_label.pack()
        self.multiplier_text.pack()

        self.encrypt_frame = EncryptFrame(self)
        self.decrypt_frame = DecryptFrame(self)
        self.encrypt_frame.pack(side=LEFT)
        self.decrypt_frame.pack(side=RIGHT)


class EncryptFrame(Subframe):
    """Layout for the element set that is needed to encrypt text"""

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
    """Layout for the element set that is needed to decrypt text"""

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
