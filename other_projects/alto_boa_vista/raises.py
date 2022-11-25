import pandas as pd

df = pd.read_excel('/home/enacom/Área de Trabalho/Willian/Enacom/Atividades/raises.xlsx')
raises = df['raise']
r_set = []
r_dict = {}
for i, r in enumerate(raises):
    k = (r.split('(')[0]).split(' ')[1]
    message = r[len(k) + 6:]
    r_set.append(k)
    if k not in r_dict.keys():
        r_dict[k] = []
    r_dict[k].append(message)

    if k == 'ConstructorException':
        print(i)
        print(r)

print(len(r_set))
print(len(set(r_set)))
for key in r_dict.keys():
    print(f'{key}: {len(r_dict[key])}')
