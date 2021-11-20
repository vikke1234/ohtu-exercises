import requests
from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    player_reader = PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players")
    player_stats = PlayerStats(player_reader)

    for player in player_stats.top_scorer_by_nationality("FIN"):
        print(player)


if __name__ == "__main__":
    main()
