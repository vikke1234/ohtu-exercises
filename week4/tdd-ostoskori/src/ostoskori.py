from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__cart: list[Ostos] = []

    def tavaroita_korissa(self):
        return self.__len__()

    def hinta(self):
        return sum([x.hinta() for x in self.__cart])

    def lisaa_tuote(self, lisattava: Tuote):
        try:
            index = self.__cart.index(lisattava)
            self.__cart[index].muuta_lukumaaraa(1)
        except ValueError:
            self.__cart.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        if poistettava in self.__cart:
            index = self.__cart.index(poistettava)
            if self.__cart[index].lukumaara() > 1:
                self.__cart[index].muuta_lukumaaraa(-1)
            else:
                self.__cart.remove(poistettava)

    def tyhjenna(self):
        self.__cart = []

    def ostokset(self):
        return self.__cart.copy()

    def __len__(self) -> int:
        return len(self.__cart)
