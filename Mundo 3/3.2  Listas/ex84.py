#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

nomePeso = []
pessoas = []
maior = menor = 0

while True:
    
    nomePeso.append(input('nome '))
    nomePeso.append(float(input('peso ')))
    
    if len(pessoas) == 0:
        maior = menor = nomePeso[1] # peso
    elif nomePeso[1] > maior:
        maior = nomePeso[1]
    elif nomePeso[1] < menor:
        menor = nomePeso[1]
    
    pessoas.append(nomePeso[:])  # todos os elementos de nomePeso
    nomePeso.clear()  # limpar a lista nomePeso
    
    cont = input('continuar? [s/n] ')
    if cont not in 'SSss': # qq outra letra além de N tbm cancela
        break
    
print('-'*100)
print(pessoas)
print(f'{len(pessoas)} registradas')


print(f'maior {maior}')
for p in pessoas:
    if p[1] == maior:
        print(p[0])
        
        
        
        
        
# não consegui e n terminei