from tkinter import Tk
from kayttoliittyma import UserInterface
from sovelluslogiikka import ApplicationLogic


def main():
    sovellus = ApplicationLogic()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = UserInterface(sovellus, window)
    kayttoliittyma.start()

    window.mainloop()

if __name__ == "__main__":
    main()
