import json
import pandas as pd
import numpy as np

# Getting data
with open("Dados_ABV.json") as file:
    f = json.load(file)

scorers = {}
yellow_cards = {}
red_cards = {}
teams = {t: [] for t in f["Rodada 1"].keys()}
for round_key in f.keys():
    for team in f[round_key].keys():
        if "Gols" in f[round_key][team].keys():
            for player in f[round_key][team]["Gols"].keys():
                if player not in scorers.keys():
                    scorers[player] = {}
                    scorers[player]["Gols"] = f[round_key][team]["Gols"][player]
                    scorers[player]["Time"] = team
                else:
                    scorers[player]["Gols"] += f[round_key][team]["Gols"][player]
                if player not in teams[team]:
                    teams[team].append(player)
        if "CA" in f[round_key][team].keys():
            for player in f[round_key][team]["CA"].keys():
                if player not in yellow_cards.keys():
                    yellow_cards[player] = {}
                    yellow_cards[player]["CA"] = f[round_key][team]["CA"][player]
                    yellow_cards[player]["Time"] = team
                else:
                    yellow_cards[player]["CA"] += f[round_key][team]["CA"][player]
                if player not in teams[team]:
                    teams[team].append(player)

# Table

scorers_table = [[s, scorers[s]['Gols'], scorers[s]['Time']] for s in scorers.keys()]
scorers_table = sorted(scorers_table, key=lambda c: c[1], reverse=True)

yc_table = [[s, yellow_cards[s]['CA'], yellow_cards[s]['Time']] for s in yellow_cards.keys()]
yc_table = sorted(yc_table, key=lambda c: c[1], reverse=True)

teams = {k: sorted(teams[k], key=lambda c: c[0]) for k in teams.keys()}

print(f"Artilharia: \n{pd.DataFrame(scorers_table, columns=['Jogador', 'Gols', 'Time'], index=np.arange(1, len(scorers_table) + 1))}\n")
print(f"Cartões Amarelos: \n{pd.DataFrame(yc_table, columns=['Jogador', 'CA', 'Time'], index=np.arange(1, len(yc_table) + 1))}\n")
print(f"Times e Jogadores: \n{teams}")
