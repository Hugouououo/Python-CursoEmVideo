#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = int(input("lado 1: "))
l2 = int(input("lado 2: "))
l3 = int(input("lado 3: "))

if l1 + l2 > l3 or l1 + l2 == l3:   #n é só isso matamaticamente mas a programação ta certo
    print("da pra formar triangulo")
else:
    print("da nao")