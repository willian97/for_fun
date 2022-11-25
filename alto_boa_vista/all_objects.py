import itertools
from datetime import datetime, timedelta


class Team:
    id_iter = itertools.count()

    def __init__(self, name: str) -> None:
        self.id_team = next(self.id_iter)
        self.name = name
        self.points = 0
        self.games = []
        self.group = None


class Group:
    id_iter = itertools.count()

    def __init__(self, name: str, teams: list[Team]) -> None:
        self.id_group = next(self.id_iter)
        self.name = name
        self.teams = teams
        self.relationship()

    def relationship(self) -> None:
        for team in self.teams:
            team.group = self

    def show_teams(self) -> list[str]:
        return [team.name for team in self.teams]


class Place:
    id_iter = itertools.count()

    def __init__(self, name: str, city: str) -> None:
        self.id_place = next(self.id_iter)
        self.name = name
        self.city = city


class Event:
    id_iter = itertools.count()

    def __init__(self, date_time: iter, place: Place) -> None:
        self.id_event = next(self.id_iter)
        self.date_time = datetime(*date_time)
        self.place = place
        self.game = None


class Game:
    id_iter = itertools.count()

    def __init__(self, team1: Team, team2: Team, event: Event) -> None:
        self.id_game = next(self.id_iter)
        self.team1 = team1
        self.team2 = team2
        self.event = event

    def relationship(self) -> None:
        self.team1.games.append(self)
        self.team2.games.append(self)
        self.event.game.append(self)


class Round:
    id_iter = itertools.count()

    def __init__(self, name: str) -> None:
        self.id_round = next(self.id_iter)
        self.name = name
