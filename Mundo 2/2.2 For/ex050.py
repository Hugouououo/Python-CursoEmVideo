#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range (1,7):
    num = int(input('[{}] Digite um número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num  #OU   soma += num
        cont = cont + 1   #OU    cont += 1
print('-> soma =', soma)
print('-> contagem =', cont)