#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower() #deixa em minúsculo

print('existem {} A na frase'.format(frase.count('a')+1))
print('a leta A aparece na posição {}'.format(frase.find('a')+1))