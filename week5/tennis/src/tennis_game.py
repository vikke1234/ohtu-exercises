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

    def get_score(self):
        score = ""
        temp_score = 0

        if self.home_score == self.away_score:
            if self.home_score == 0:
                score = "Love-All"
            elif self.home_score == 1:
                score = "Fifteen-All"
            elif self.home_score == 2:
                score = "Thirty-All"
            elif self.home_score == 3:
                score = "Forty-All"
            else:
                score = "Deuce"

        elif self.home_score >= 4 or self.away_score >= 4:
            minus_result = self.home_score - self. away_score

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            points_to_str = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
            score = "{}-{}".format(points_to_str[self.home_score], points_to_str[self.away_score])
        return score
