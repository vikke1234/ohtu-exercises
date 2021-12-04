from enum import Enum
from tkinter import ttk, constants, StringVar

from sovelluslogiikka import Sovelluslogiikka


class Command(Enum):
    SUM = 1
    DIFF = 2
    ZERO = 3
    CLEAR = 4


class UserInterface:
    def __init__(self, sovellus: Sovelluslogiikka, root):
        self._application = sovellus
        self._root = root

    def start(self):
        self._output_var = StringVar()
        self._output_var.set(self._application.value)
        self._input_field = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._output_var)

        addition_button = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._run_command(Command.SUM)
        )

        subtract_button = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._run_command(Command.DIFF)
        )

        self._zero_button = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._run_command(Command.ZERO)
        )

        self._clear_button = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._run_command(Command.CLEAR)
        )

        tulos_teksti.grid(columnspan=4)
        self._input_field.grid(columnspan=4, sticky=(constants.E, constants.W))
        addition_button.grid(row=2, column=0)
        subtract_button.grid(row=2, column=1)
        self._zero_button.grid(row=2, column=2)
        self._clear_button.grid(row=2, column=3)

    def _run_command(self, command):
        value = 0
        commands = {Command.SUM: self._application.add, Command.DIFF: self._application.subtract, Command.CLEAR: self._application.zero, Command.ZERO: self._application.zero}
        try:
            value = int(self._input_field.get())
        except Exception:
            pass

        commands[command](value)

        self._clear_button["state"] = constants.NORMAL

        if self._application.value == 0:
            self._zero_button["state"] = constants.DISABLED
        else:
            self._zero_button["state"] = constants.NORMAL

        self._input_field.delete(0, constants.END)
        self._output_var.set(self._application.value)
