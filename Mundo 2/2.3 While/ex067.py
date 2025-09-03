#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um número e veja sua tabuada: '))
    if n > 0:
        print(f'--Tábuada do {n}--')
        for m in range(1,11):
            print(f'{n} x {m} = {n*m}')
        print('-'*16)
    else:
        print('-'*25, 'ERRO', '-'*25)
        print('O número digitado foi negativo. Encerrando programa...')
        print('-'*56)
        break
