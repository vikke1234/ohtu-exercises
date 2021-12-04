class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.value: int = tulos

    def subtract(self, arvo):
        self.value = self.value - arvo

    def add(self, arvo):
        self.value = self.value + arvo

    def zero(self, _ = 0):
        # _ is to simply all functions have equal arguments
        self.value = 0

    def set_value(self, value):
        self.value = value
