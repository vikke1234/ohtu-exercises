class Player:
    def __init__(self, player_dict: dict):
        for k, v in player_dict.items():
            setattr(self, k, v)

    def __str__(self):
        return f"{self.name:20} team {self.team} goals {self.goals} assists {self.assists}"

