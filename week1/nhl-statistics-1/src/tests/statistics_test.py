import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
                Player("Semenko", "EDM", 4, 12),
                Player("Lemieux", "PIT", 45, 54),
                Player("Kurri",   "EDM", 37, 53),
                Player("Yzerman", "DET", 42, 56),
                Player("Gretzky", "EDM", 35, 89)
            ]

class TestStatistics(unittest.TestCase):
    def setUp(self) -> None:
        self.stat = Statistics(PlayerReaderStub())
    
    def test_search_existing_player(self):
        p = self.stat.search("Semenko")
        self.assertEqual(p.name, "Semenko")
    
    def test_search_nonexisting_player(self):
        p = self.stat.search("htneaodutnhoedau")
        self.assertEqual(p, None)

    def test_get_team(self):
        team = self.stat.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_scorers(self):
        top = self.stat.top_scorers(1)
        self.assertEqual(top[0].name, "Gretzky")

