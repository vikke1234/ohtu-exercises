# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, max_size):
        self._max_size = max_size
        self._memory = []

    def aseta_siirto(self, move):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        if len(self._memory) == self._max_size:
            self._memory = self._memory[1:]
        self._memory.append(move)

    def anna_siirto(self):
        if len(self._memory) < 2:
            return "k"

        previous_move = self._memory[0]

        k = 0
        p = 0
        s = 0
        for i in range(len(self._memory) - 1):
            if previous_move == self._memory[i]:
                next_move = self._memory[i + 1]

                if next_move == "k":
                    k = k + 1
                elif next_move == "p":
                    p = p + 1
                else:
                    s = s + 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return "p"
        elif p > k or p > s:
            return "s"
        else:
            return "k"


class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
