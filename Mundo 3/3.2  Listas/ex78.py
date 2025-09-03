#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()

n = int(input('Digite o 1º número:'))
lista.append(n)

maior = menor = n

for c in range(1,5):
    
    n = int(input(f'Digite o {c+1}º número:'))
    lista.append(n)
    
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
        
print(f'lista = {lista}')

print(f'Maior numero {maior} na posição / posições: ', end='')
for pos, val in enumerate(lista):
    if val == maior:
        print(pos+1, end=' ')
        
print()

print(f'menor numero {menor} na posição / posições: ', end='')
for pos, val in enumerate(lista):
    if val == menor:
        print(pos+1, end=' ')