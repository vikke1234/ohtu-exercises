class All:
    def __init__(self, *_):
        pass

    def matches(self, _):
        return True

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False

        return True

class Or:
    def __init__(self, *matchers) -> None:
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False

class Not:
    def __init__(self, match) -> None:
        self._match = match

    def matches(self, player):
        return not self._match.matches(player)


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self.at_least = HasAtLeast(value, attr)

    def matches(self, player):
        return not self.at_least.matches(player)

class QueryBuilder:
    def __init__(self, query = All()) -> None:
        self._query = query

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))

    def plays_in(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def one_of(self, *queries):
        return QueryBuilder(Or(*queries))

    def build(self):
        return self._query
