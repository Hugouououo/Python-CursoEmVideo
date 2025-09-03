#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaPar = []
listaImpar = []
# não funciona se escrever assim:  lista = listaPar = listaImpar = []

while True:
    
    n = int(input('Digite um número: '))
    lista.append(n)
    
    if n != 0: 
        if n % 2 == 0:
            listaPar.append(n)
        else: 
            listaImpar.append(n)
            
    cont = input('Deseja continuar? [s/n]: ')
    if cont not in 'SSss':
        break
    
print('-'*20)
print(f'Lista completa: {lista}')
print(f'Lista apenas com os números pares: {listaPar}')
print(f'Lista apenas com os números ímpares: {listaImpar}')

    
    