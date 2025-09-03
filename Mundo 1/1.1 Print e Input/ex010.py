#leia quanto de dinheiro uma pessoa tem na carteira  e quantos dólares ela pode comprar
#considerar: 1 dolár = 5 reais (janeiro/2023)

money = float(input('Insira a quantia a transformar para dólares: R$'))

dol = money / 5.09
#eur = money / 5.52
#yen = money / 0.040
#lib = money / 0.028
#pes = money / 6.22

print('-'*15)

print('$1 = R$5.09 | (Jan/2023)')
print('Sua quantia em dóllares é: ${:.2}'.format(dol))

print('-'*15)