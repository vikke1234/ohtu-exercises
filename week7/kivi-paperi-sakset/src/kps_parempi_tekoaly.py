from player import Player
from tuomari import Judge
from tekoaly import TekoalyParannettu


class KPSParempiTekoaly(Player):
    def __init__(self) -> None:
        super().__init__()
        self.bot = TekoalyParannettu(10)

    def get_player_input(self):
        p1 = input("Player 1 move: ")
        p2 = self.bot.anna_siirto()
        self.bot.aseta_siirto(p1)
        print(f"The AI chose: {p2}")

        return p1, p2

