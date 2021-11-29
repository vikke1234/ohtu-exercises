from tuote import Tuote

class Ostos:
    def __init__(self, tuote: Tuote):
        self.tuote = tuote
        self._lukumaara = 1

    def tuotteen_nimi(self) -> str:
        return self.tuote.nimi()

    def muuta_lukumaaraa(self, muutos: int):
        self._lukumaara += muutos
        if self._lukumaara<0:
            self._lukumaara = 0

    def lukumaara(self):
        return self._lukumaara

    def hinta(self):
        return self._lukumaara * self.tuote.hinta()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Tuote):
            return self.tuote == o

        elif isinstance(o, Ostos):
            return self.tuote == o.tuote

        return False
