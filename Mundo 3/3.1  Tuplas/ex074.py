#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
from random import randint

num = tuple(randint(1,100) for n in range(0,5)) # tuple() junta as variáveis em uma tupla

print('Tupla:')
for n in range(0,5):
    print(num[n])

print(f'Maior número da tupla: {max(num)}') # max() mostra o maior número de uma tupla,lista, etc...
print(f'Menor número da tupla: {min(num)}') # e min() mostra o menor.