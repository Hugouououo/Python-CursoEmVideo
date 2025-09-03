#leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

sal = float(input('Digite seu salário: R$'))

aum = sal * 15/100
final = sal + aum

print('Aumento: {} \nSalário final: {}'.format(aum, final))