#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('digite seu nome completo: ')).split()

print(nome[0])
print(nome[len(nome)-1])
