#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# matriz = []
# linha = 1
# coluna = 1

# for c in range(9):
    
#     matriz.append(int(input(f'Digite o número da {linha}ª linha, {coluna}ª coluna: ')))
    
#     coluna += 1
#     if coluna == 4:
#         coluna = 1
#         linha += 1
        
# # com certeza isso aqui é um jeito bem preguiçoso
# print(matriz[0], matriz[1], matriz[2])
# print(matriz[3], matriz[4], matriz[5])
# print(matriz[6], matriz[7], matriz[8])



# SOLUÇÃO DO GUANABARA:
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
        
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()