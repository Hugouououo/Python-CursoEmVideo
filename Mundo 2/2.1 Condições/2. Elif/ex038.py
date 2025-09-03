#Escreva um programa que leia dois números inteiros e compare-os.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1,num2))

elif num2 > num1:
    print('{} é maior que {}'.format(num2,num1))

elif num2 == num1 or num1 == num2:
    print('Os dois são iguais')
