# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
numero = num % 2

if numero == 0:
    print('par')

else:
    print('impar')