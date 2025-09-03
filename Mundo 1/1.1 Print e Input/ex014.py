#conversor de temperaturas: C -> F

c = float(input('Digite uma temperatura em ºC: '))

#Equação de Celsius para Farenheit
f = ((c * 9) / 5) + 32  # <- funciona sem parênteses pela ordem de precedência

print('A temperatura de {}ºC em Farenheit é: {}ºF'.format(c,f))