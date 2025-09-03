#leia a altura e largura de uma parede em metros, calcule sua área e a
#quantidade de tinta necessária para pinta-lá
#litro de tinta = 2m²

larg = float(input('Qual a largura da parede?(em metros): '))
comp = float(input('Qual o comprimento da parede?(em metros):'))

tint = (larg*comp) / 2

print('-'*50)
print('Dimensões da parede: {} x {} = {:.3}m²'.format(larg,comp,larg*comp))
print('Quantidade necessária de tinta: {:.3} litros'.format(tint))
print('-'*50)