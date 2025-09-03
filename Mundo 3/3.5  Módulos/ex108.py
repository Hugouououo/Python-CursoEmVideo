# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda108

p = float(input('Digite o preço: R$ '))
t = int(input('Digite a taxa (%): '))

print(f'Com um aumento de {t}%, temos {moeda108.format(moeda108.aumentar(p))}')
print(f'Com um desconto de {t}%, temos {moeda108.format(moeda108.diminuir(p))}')
print(f'O dobro de {moeda108.format(p)} é {moeda108.format(moeda108.dobro(p))}')
print(f'A metade de {moeda108.format(p)} é {moeda108.format(moeda108.metade(p))}')


