#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep  #espera
import emoji    #emoji.emojize

print('CONTAGEM REGRESSIVA!')
for c in range (10, -1, -1):   #-1 pq o 0 seria ignorado  /  -1 significa diminuição
    print(c)
    sleep(0.5)
print(emoji.emojize('acabou! :fireworks:'))