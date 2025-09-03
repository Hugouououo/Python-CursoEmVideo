#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Escolha a base númerica para a conversão:
[1] Binário
[2] Hexadecimal
[3] Octal''')
op = int(input('Digite sua opção: '))

if op == 1:
    print('Seu número é: {}'.format(bin(num)[2:])) #BINÁRIO
elif op == 2:
    print('Seu número é: {}'.format(hex(num)[2:])) #HEXADECIMAL
elif op == 3:
    print('Seu número é: {}'.format(oct(num)[2:])) #OCTAL
else:
    print('Opção inválida, tente usar uma das opções listadas.')