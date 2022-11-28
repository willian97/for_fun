from utils import *
from all_objects import *

number_of_teams = 32
number_of_groups = 8
teams_to_kncockout = 16
stadiums = [('Alto do Boa Vista', 'Mateus Leme')]
time_of_games = {'sunday': ['09:00', '11:00', '13:00', '15:00']}
days_of_games = {'start': '04/12/2022', 'days': ['sunday'], 'invalid_days': ['25/12/2022', '01/01/2023']}

teams_names = generic_teams_names(number_of_teams)
teams_by_group = teams_by_group_array(number_of_teams, number_of_groups)
rounds_games = calculate_rounds_and_games(number_of_teams, number_of_groups, teams_to_kncockout)
rounds = build_rounds(rounds_games[0][1])
places = [Place(*s) for s in stadiums]
groups = build_groups(teams_names, teams_by_group)

summary = {'places': places,
           'groups': groups}

for g in summary['groups']:
    print(g.teams[0].group.name)
    print(g.show_teams())

print(f'rounds: {[r.name for r in rounds]}')
