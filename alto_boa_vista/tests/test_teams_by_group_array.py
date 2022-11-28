import pytest
from utils import Utils
import numpy as np


@pytest.mark.parametrize(
    "nteams, ngroups",
    [[4, 4], [11, 5], [93, 8], [32, 17], [45, 46]]
)
def test_number_of_groups_must_by_equal_ngroups(nteams: int, ngroups: int):
    expected = ngroups
    actual = len(Utils.teams_by_group_array(nteams, ngroups))

    assert expected == actual


@pytest.mark.parametrize(
    "nteams, ngroups",
    [[5, 5], [10, 5], [100, 2], [32, 8], [9, 3]]
)
def test_number_of_teams_is_divisible_by_number_of_groups_return_same_number_of_teams_by_group(nteams: int,
                                                                                               ngroups: int):
    """
    Test if when we divide the teams by group and the number of teams is divisble by number of groups is returned the
    same number of teams by group, with ngroups groups.

    :param nteams: number of teams
    :param ngroups: number of groups
    """
    expected = np.array([nteams / ngroups] * ngroups)
    actual = Utils.teams_by_group_array(nteams, ngroups)

    np.testing.assert_equal(actual, expected)



