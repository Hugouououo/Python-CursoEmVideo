#Leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0

n = int(input('Digite um número (Digite 999 para encerrar): ')) 
# tá aqui em cima e n direto dentro do while porque se tivesse o flag (999) seria somado

while n != 999:
    soma = soma + n
    cont += 1
    n = int(input('Digite um número (Digite 999 para encerrar): '))
    
if soma == 0 and n == 999:
    print('Nenhum número digitado...')
else:
    print("Soma de todos os numeros: {}".format(soma))
print("Quantidades de números: {}".format(cont))