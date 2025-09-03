#algoritmo que leia um preço de um produto e mostre seu preço com 5% de desconto na liquidação

preço = float(input('Digite um preço para calcular o desconto: R$'))

liq = preço * 5/100

print('Na liquidação, você terá um desconto de: R${:.2f}'.format(liq))