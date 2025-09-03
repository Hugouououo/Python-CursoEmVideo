#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint ; from time import sleep

j = int(input('Quantos jogos serão gerados?: '))
lista = list()

for pos in range(j):
    
    lista.append([])
    
    for c in range(0,6):
    
        n = randint(1,60)
        while n in lista[pos]:
            n = randint(1,60)
            
        lista[pos].append(n)
            
    lista[pos].sort()
    print(f'{pos+1}º Jogo: {lista[pos]}')
    
    sleep(0.5)
