# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
jogadores = {}


for c in range(1,5):
    jogadores[f'Jogador{c}'] = randint(1,20)
    
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# cont = 1
# for k, v in jogadores.items():
#     print(f'{cont}º lugar: {k} [{v}]')
#     cont += 1

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} [{v[1]}]')