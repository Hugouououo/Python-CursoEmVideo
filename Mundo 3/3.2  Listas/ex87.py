#Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

# usando a solução do guanabara do ex86:
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = soma3 = maior2 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
        
        # A)
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        # B)
        if c == 2:
            soma3 += matriz[l][c]
# C)
for c in range(0,3):
    if c == 0 or matriz[1][c] > maior2:
        maior2 = matriz[1][c]
    
        
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')           
    print()

print(f' A) soma par: {somaPar}')
print(f' B) soma dos valores da terceira coluna: {soma3}')
print(f' C) maior valor da segunda linha: {maior2}')
