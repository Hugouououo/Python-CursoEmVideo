#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

pal = 'PROGRAMAR'

print('Na palavra "PROGRAMAR" temos as vogais: ', end='')

for letra in pal.upper():
    if letra in 'AEIOU':
        print(letra, end=', ')