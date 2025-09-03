#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0  #Acumulador

for c in range (1, 501, 2):    #pulando de 2 em 2 pq é impar
 if c % 3 == 0:
  soma = soma + c
print(soma) #= 20667
