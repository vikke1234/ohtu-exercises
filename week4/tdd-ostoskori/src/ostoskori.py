from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__cart: list[Ostos] = []

    def tavaroita_korissa(self):
        pass

    def hinta(self):
        return 0

    def lisaa_tuote(self, lisattava: Tuote):
        pass

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        pass

