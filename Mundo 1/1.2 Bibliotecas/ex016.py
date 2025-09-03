from math import ceil,floor,trunc

num = float(input('Digite um número com casas decimais:'))

print("-"*15)
print('Seu número: {}\nArredondado pra baixo: {}\nArredondado pra cima: {}\nValor inteiro: {}'.format(num,floor(num),ceil(num),trunc(num)))
print("-"*15)

#Funciona com o Int tambem, sem importar bibliotecas