from tuomari import Judge


class Player:
    def __init__(self) -> None:
        self.judge = Judge()

    def pelaa(self):
        p1_move, p2_move = self.get_player_input()

        while self._move_ok(p1_move) and self._move_ok(p2_move):
            self.judge.log_move(p1_move, p2_move)
            print(self.judge)

            p1_move, p2_move = self.get_player_input()

    def get_player_input(self):
        raise NotImplementedError("Implement how to get player input")

    def _move_ok(self, move):
        return move == "k" or move == "p" or move == "s"
