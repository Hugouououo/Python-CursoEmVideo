#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = soma = cont = 0

print('Digite 000 para parar...')

while True:
    n = int(input('Digite um número: '))
    if n == 000:
        break
    soma += n
    cont += 1
    
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')