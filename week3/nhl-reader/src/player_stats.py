from player import Player
from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, player_reader: PlayerReader) -> None:
        self.players = []
        for player_dict in player_reader.get_players():
            self.players.append(Player(player_dict))

    def top_scorer_by_nationality(self, nationality: str):
        return sorted(filter(lambda p: p.nationality == nationality, self.players), key=lambda p: p.goals + p.assists)
