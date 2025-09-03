#ler o comprimento do cateto adj. e do cateto op. e calcular a hipotenusa
from math import hypot

op = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("Digite o comprimento do cateto adjacente: "))
#hip = (co**2 + adj**2) ** 1/2 (<-raiz quadrada)               [jeito matemático]
hip = hypot(op,adj)

print("A hipotenusa é {:.2f}".format(hip))