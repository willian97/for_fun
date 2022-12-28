import numpy as np


odds = [2.22, 2.05, 8]
M = 300

b = 1 / (1 + odds[1] / odds[0] + odds[1] / odds[2])
a = b * odds[1] / odds[0]
c = b * odds[1] / odds[2]

bets = M * np.array([a, b, c])
total = bets * np.array(odds)
print(f"Cash: R${M}")
print(f"ideal bets (R$) {bets}")
print(f"ideal return (R$) {total}")


effective_bets = np.ceil(np.array([189, 74, 38]))
effective_return = effective_bets * np.array(odds)
sum_bets = sum(effective_bets)
print((total - M) / M)
print(f"cash: {round(100 * max(total - M) / M, 2)}%, R${round(max(total) - M, 2)}")
print(f"effective bets: {effective_bets}")
print(f"effective return: {effective_return}")
print(f"sum bets: {sum_bets}")
print(f"max: {round(100 * (max(effective_return) - sum_bets) / sum_bets, 2)}%, "
      f"R${round(max(effective_return) - sum_bets, 2)}")
print(f"min: {round(100 * (min(effective_return) - sum_bets) / sum_bets, 2)}%, "
      f"R${round(min(effective_return) - sum_bets, 2)}")
