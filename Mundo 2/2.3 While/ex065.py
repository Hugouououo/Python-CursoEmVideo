#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = n = cont = maior = menor = 0     #todas as variaveis recebem 0
continuar = 's'

while continuar == 's':
    n = int(input('Digite um número'))
    continuar = str(input('Quer continuar? [s/n]: ')).lower().strip()
    soma = soma + n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
media = soma / cont
print('Média de todos os números: {}'.format(media))
print('O menor numero foi {} e o maior foi {}'.format(menor, maior))
    

