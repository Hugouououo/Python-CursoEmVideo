# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

tup = tuple(int(input('Digite um número: ')) for c in range(1,5))

print(f'O valor 9 foi digitado {tup.count(9)} vezes.')

if 3 in tup:
    print(f'O valor 3 está na {tup.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

print('Os valores pares digitados foram: ', end='')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')