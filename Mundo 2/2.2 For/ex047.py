#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep

for par in range (1, 51):
    if par % 2 == 0:              #se o RESTO for 0 é par
        print(par)
        sleep(0.4)

#tbm pode-se usar  range(2, 51, 2)  <- pulando de 2 em 2  [MAIS EFICIENTE, menos trabalho]