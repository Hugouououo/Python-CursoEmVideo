#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando while.

t = int(input("digite o primeiro termo: "))
r = int(input("digite a razão: "))

c = 1

print(t)
while c <= 10:
    print(t * (r * c))
    c += 1 