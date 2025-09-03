#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))

if n1 > n2 > n3:
    print("um", n1, n3)
elif n1 < n2 < n3:
    print("dois", n3, n1)
elif n1 > n2 < n3:
    print("tres", n1, n2)
elif n1 < n2 > n3:
    print("quatro", n2, n3)
else:
    print("algo deu errado")