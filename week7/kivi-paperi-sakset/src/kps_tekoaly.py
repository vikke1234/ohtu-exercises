from player import Player
from tuomari import Judge
from tekoaly import Tekoaly


class KPSTekoaly(Player):
    def __init__(self) -> None:
        super().__init__()
        self.bot = Tekoaly()


    def get_player_input(self):
        p1 = input("Player 1 move: ")
        p2 = self.bot.anna_siirto()

        print(f"The bot chose: {p2}")
        return p1, p2
