#Crie um programa onde o usuário possa digitar CINCO valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
# Resolução do Guanabara, não consegui fazer.

lista = []

for c in range(0,5):
    
    n = int(input('Digite um número:'))
    
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no fim da lista')
    else:
        pos = 0
        while pos < len(lista):
            
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos}')
                break
            
            pos += 1

    print(lista)
print('Fim')
    
    
    
    
    
    
    
    
    
    

    
################ Tentativa 1 ##################
# if n > maior:
#     lista.insert(lista.index(maior)+1, n)
#     maior = n
# elif n < menor:
#     lista.insert(lista.index(menor)-1, n)
#     menor = n
################ Tentativa 2 ##################
# if n > anterior:
#     lista.insert(lista.index(anterior)+1, n)
# elif n < anterior:
#     lista.insert(lista.index(anterior)-1, n)
# elif n == anterior:
#     lista.insert(lista.index(anterior)+1, n)
###############################################