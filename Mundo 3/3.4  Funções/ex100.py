#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
sorteados = []

def sortear(sorteados):
    print('Seus valores sorteados foram: ')
    for c in range(0,5):
        sorteados.append(randint(00,99))
        print(sorteados[c] , end=' ')
    print()
    
def somaPar(sorteados):
    soma = 0
    for valor in sorteados:
        if valor % 2 == 0:
            soma += valor                                   # "valor" é melhor que "sorteados[c]" burro
    print(f"A soma dos valores pares foi: {soma}")
    
sortear(sorteados)
somaPar(sorteados)
    