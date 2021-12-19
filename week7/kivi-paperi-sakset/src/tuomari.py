
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Judge:
    def __init__(self):
        self.player1_points = 0
        self.player2_points = 0
        self.tasapelit = 0

    def log_move(self, ekan_siirto, tokan_siirto):
        if self._draw(ekan_siirto, tokan_siirto):
            self.tasapelit += 1
        elif self._player1_win(ekan_siirto, tokan_siirto):
            self.player1_points += 1
        else:
            self.player2_points += 1

    def __str__(self):
        return f"Pelitilanne: {self.player1_points} - {self.player2_points}\nTasapelit: {self.tasapelit}"

    # sisäinen metodi, jolla tarkastetaan tuliko tasapeli
    def _draw(self, player1, player2):
        return player1 == player2

    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _player1_win(self, player1, player2):
        counters = {"k": "s", "s": "p", "p": "k"}
        return counters[player1] == player2
