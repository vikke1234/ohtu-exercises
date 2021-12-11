from statistics import Statistics
from player_reader import PlayerReader
from matchers import *

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    m1 = query.plays_in("PHI").has_at_least(10, "assists").has_fewer_than(5, "goals").build()
    m2 = query.plays_in("EDM").has_at_least(40, "points").build()

    matcher = query.one_of(
            query.plays_in("EDM").has_at_least(40, "points").build(),
            query.plays_in("PHI").has_at_least(10, "assists").has_fewer_than(5, "goals").build()).build()
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
