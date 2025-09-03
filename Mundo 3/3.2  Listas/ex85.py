# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

total = [[], []]

for c in range(7):
    
    n = int(input('numero '))
    if n != 0:
        if n % 2 == 0:
            total[0].append(n)
        else:
            total[1].append(n)
    else:
        print('0 não é aceito')
        
total[0].sort()
total[1].sort()

print(f'par: {total[0]}')
print(f'impar: {total[1]}')
