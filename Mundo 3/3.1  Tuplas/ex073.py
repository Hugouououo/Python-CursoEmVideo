#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
# pra n ter que escrever os times eu vo escrever os nomes de personagens do lol em ordem de maestria

lol = ('Rakan','Kayn','Varus','Viego','Mordekaiser','Yone','Viktor','Xayah','Sett')

print('='*100)
print(lol)
print('-'*100)
print(f'Ordem alfabética: {sorted(lol)}')
print('-'*100)
print(f'3 maiores maestrias: {lol[0:3]}')
print('-'*100)
print(f'O Mordekaiser está {lol.index("Mordekaiser")}ª posição')
print('='*100)