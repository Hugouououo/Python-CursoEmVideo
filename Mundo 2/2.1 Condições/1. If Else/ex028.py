#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep      #usado na linha 9
             #usado na linha 13 com   emoji.emojize(:thumbs_up:)

num = randint(0,5)

esc = int(input('Descubra qual é o número de 0 a 5: '))
print('Processando...')
sleep(1)  #em segundos

if esc == num:
    print('vc acertou :thumbs_up:')
else:
    print('vc errou')