from tuomari import Judge
from player import Player


class KPSPelaajaVsPelaaja(Player):
    def get_player_input(self):
        p1 = input("Player 1 move: ")
        p2 = input("Player 2 move: ")
        return p1, p2
