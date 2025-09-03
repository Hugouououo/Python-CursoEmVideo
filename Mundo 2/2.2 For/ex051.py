#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão:'))
cont = 0

print(termo)
for PA in range (1, 10):
    cont += 1
    print(termo + (raz*cont))


# Progressão aritmética funcional