#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite seu número: '))
#n = str(num)

print(num // 1 % 10) #uni
print(num // 10 % 10) #dez
print(num // 100 % 10) #cen
print(num // 1000 % 10) #mil