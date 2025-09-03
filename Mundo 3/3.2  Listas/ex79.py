#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista = []

while True:
    n = int(input('Digite um número: '))

    if n in lista:
        print('Você já digitou esse número. ', end='')
    else:
        lista.append(n)
    
    continuar = str(input('Deseja continuar? [s/n]: '))
    if continuar in "NNnn":
        break
    
print('Sua lista em ordem crescente é: ')
lista.sort()
print(lista)