#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tup = ('Hugo',18,'Julia',18,'Pedro',19,'Flávia',18,'Lucas',18,'Yuri',19)

print('-'*20)
print(f'{'Amigos e Idades' :^20}')
print('-'*20)

for pos in range(0, len(tup)):
    if pos % 2 == 0:
        print(f'{tup[pos] :<13}', end='')
    else:
        print(f'{tup[pos] :>5}')

print('-'*20)