#faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

pi = str(input('Par ou Impar? [p/i]: ')).lower().strip()
jgN = int(input('Digite seu número de 0 a 5: '))                            # PROBLEMA AQUI
pcN = randint(0,5)
ganhou = True
vitórias = 0

print(f'Soma = {jgN+pcN}')  
result = (jgN + pcN) % 2

if pi == 'p' or pi == 'i':                                              # PROBLEMA AQUI
    
    while ganhou == True:
        if pi == 'p' and result == 0 or pi == 'i' and result != 0:
            print('Jogador ganhou')
            ganhou = True
            vitórias += 1
            
            print('---- REVANCHE!!! ----')
            pi = str(input('Par ou Impar? [p/i]: ')).lower().strip()
            jgN = int(input('Digite seu número de 0 a 5: '))        
        else:
            print('Computador ganhou')
            ganhou = False
            break
        
    print(f'Você ganhou {vitórias} vezes seguidas!')
    print('Fim de jogo...')
    
else:
    print('erro, digite certo >:|')
    pi = str(input('Par ou Impar? [p/i]')).lower().strip()  
