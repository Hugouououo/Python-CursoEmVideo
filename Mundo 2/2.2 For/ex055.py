#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input("digite o peso da {}ª pessoa: ".format(p)))

    if p == 1:
        maior = peso     # o primeiro valor sempre vai ser o maior e o menor valor enquanto nâo houver outro
        menor = peso
    else:
        if peso > maior:    # se o peso novo é maior que o maior anterior, ele é o novo maior
            maior = peso
        elif peso < menor:  # se o peso novo é menor que o menor anterior, ele é o novo maior
            menor = peso
        else:
            print('erro')

print('maior peso = ', maior)
print('menor peso = ', menor)
