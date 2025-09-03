# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador = '<desconhecido>', gols = '<não_informado>'):
    print(f'O jogador {jogador} marcou {gols} gols')
    
n = str(input('Digite o nom do jogador: '))
g = input('Digite quantos gols foram feitos: ')

if g.isnumeric():
    g = int(g)
else:
    ficha(n)
    
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
