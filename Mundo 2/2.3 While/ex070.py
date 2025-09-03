#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: 
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

print('-'*10, 'Lista de Compras', '-'*10)

nome = str(input('Nome: '))
preco = float(input('Preço: '))

barato = menor = prod = soma = 0
menor = preco

while True:
    
    if preco >= 0:       
        if menor < preco:
            menor = preco
            barato = nome
        
        if preco > 1000:
            prod += 1
            
        soma = soma + preco
        
        continuar = str(input('Quer continuar> [s/n]: ')).lower().strip()[0]
        if continuar == 'n':
            print('-'*10, 'Encerrando o programa', '-'*10)
            break
        elif continuar not in 'sn':
            print('* Resposta inválida... * ')
            print('-'*10, 'Encerrando o programa', '-'*10)
            break
        
        nome = str(input('Nome: '))
        preco = float(input('Preço: '))

    else:
        print('Preço inválido, tente novamente...')
    
print(f'A soma total dos produtos foi de R${soma :.2f}')

if prod > 0:
    print(f'Há {prod} produto que custa mais de R$1000.00')
    
print(f'O produto mais barato da lista foi: {barato}, que custa R${menor :.2f}')