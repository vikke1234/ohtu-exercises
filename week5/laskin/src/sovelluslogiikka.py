class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def subtract(self, arvo):
        self.tulos = self.tulos - arvo

    def add(self, arvo):
        self.tulos = self.tulos + arvo

    def clear(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
