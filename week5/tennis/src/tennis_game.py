class TennisGame:
    def __init__(self, home, away):
        self.home = home
        self.away = away
        self.home_score = 0
        self.away_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.home_score = self.home_score + 1
        else:
            self.away_score = self.away_score + 1

    def __check_deuce(self):
        diff = self.home_score - self. away_score

        if diff == 1:
            return "Advantage player1"
        elif diff == -1:
            return "Advantage player2"
        elif diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"


    def get_score(self):
        score = ""
        points_to_str = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

        if self.home_score == self.away_score:
            if self.home_score in points_to_str:
                score = f"{points_to_str[self.home_score]}-All"
            else:
                score = "Deuce"

        elif self.home_score >= 4 or self.away_score >= 4:
            score = self.__check_deuce()

        else:
            score = f"{points_to_str[self.home_score]}-{points_to_str[self.away_score]}"

        return score
