#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um numero pra ve se é primor: "))

if n % 2 == 0:
    print("é nada")
else:
    print("é sim")