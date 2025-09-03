# Crie um módulo chamado moeda107.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda107

p = str(input('Digite o preço: R$ ')).replace(',' , '.')
p = float(p)

t = int(input('Digite a taxa (%): '))

moeda107.aumentar(p, t)
moeda107.diminuir(p, t)
moeda107.dobro(p)
moeda107.metade(p)
