import math
from typing import Any
import string

import numpy as np
from numpy import ndarray
from all_objects import *


def calculate_rounds_and_games(n_teams: int,
                               n_groups: int,
                               n_star: int,
                               same_teams: int = 1,
                               games_knockout: int = 1,
                               games_final: int = 1) -> tuple[list[ndarray | list[float | int | Any]], int]:
    """
    Calculate the total number of rounds and games of tournament. Also, it calculates the rounds by stage.

    :param n_teams: number of teams.
    :param n_groups: number of groups.
    :param n_star: number of teams that advance to knock-out stage.
    :param same_teams: number of times that teams play with each opponent in group stage.
    :param games_knockout: number of times that teams play with opponent in each knock-out stage.
    :param games_final: number of final games.
    :return: number_of_rounds: the number of rounds in the tournament.
    :return: rounds_by_stage: the number of rounds by stage (group, knock-out).
    :return: number_of_games: the total number of games in tournament.
    """
    tbg = teams_by_group_array(n_teams, n_groups)
    rounds_group_stage = [number - 1 + number % 2 for number in tbg]
    rounds_knockout_stage = math.log(n_star, 2)
    rounds_by_stage = [max(rounds_group_stage) * same_teams, rounds_knockout_stage]
    number_of_rounds = np.sum(rounds_by_stage)

    games_group_stage = [(number ** 2 - number) / 2 for number in tbg]
    gg = np.sum(games_group_stage) * same_teams
    number_of_games = gg + (rounds_knockout_stage - 1) * games_knockout + games_final
    return [number_of_rounds, rounds_by_stage], number_of_games


def teams_by_group_array(n_teams: int, n_groups: int) -> list[int]:
    """
    Creates an array with number of teams by group.

    :param n_teams: number of teams
    :param n_groups: number of groups
    :return: number of teams by group
    """
    n_teams_by_group = np.array([n_teams // n_groups] * n_groups)
    n_teams_by_group[:n_teams % n_groups] += 1
    return n_teams_by_group[::-1]


def build_rounds(rounds: list[int]) -> list[Round]:
    """
    Builds the Round object for each round on the tournament.

    :param rounds: names of rounds.
    :return: Round list.
    """
    result = []
    for r in range(rounds[0]):
        result.append(Round('round ' + str(r + 1)))
    for r in range(int(rounds[1])):
        if r + 1 == rounds[1]:
            name = 'final'
        elif r + 2 == rounds[1]:
            name = 'semi-final'
        elif r + 3 == rounds[1]:
            name = 'quarter-finals'
        else:
            name = 'round of ' + str(int(2 ** (rounds[1] - r)))
        result.append(Round(name))
    return result


def build_groups(teams_names: list[str],
                 teams_by_group: list[int]) -> list[Group]:
    """
    Builds the groups of tournament.

    :param teams_names: name of teams.
    :param teams_by_group: number of teams by group.
    :return: Group list.
    """
    group_index = 1
    groups = {}
    list_of_groups = []
    while len(teams_names) > 0:
        index_team = np.random.choice(np.arange(len(teams_names)))
        choose_name = teams_names.pop(index_team)
        if ('Grupo ' + str(group_index)) not in groups.keys():
            groups['Grupo ' + str(group_index)] = []
        groups['Grupo ' + str(group_index)].append(Team(choose_name))
        if len(groups['Grupo ' + str(group_index)]) == teams_by_group[group_index - 1]:
            group_index += 1

    for key in groups.keys():
        list_of_groups.append(Group(key, groups[key]))
    return list_of_groups


def generic_teams_names(number_of_teams: int) -> list[str]:
    """
    Creates the generic names of teams.

    :param number_of_teams: number of teams.
    :return: The generic names of teams.
    """
    teams_names = ['Time ' + item for item in list(string.ascii_uppercase)[:number_of_teams]]
    if len(teams_names) < number_of_teams:
        rest_teams = ['Time ' + str(item) for item in range(number_of_teams - len(teams_names))]
        teams_names.extend(rest_teams)
    return teams_names
