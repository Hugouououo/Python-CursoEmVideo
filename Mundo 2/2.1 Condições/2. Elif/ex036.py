#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa?: '))
sal = int(input('Coloque seu salário: '))
anos = int(input('Em quantos anos você irá pagar?: '))

prest = (casa / anos) / 12
print('Prestação mensal: R${:.2f}'.format(prest))

if prest > (sal * 30 / 100):
    print('Você não consegue empréstimo pela prestação ser maior que 30porcento do seu salário.')
elif prest == (sal * 30 / 100):
    print('Você consegue empréstimo com a prestação máxima dentro do seu salário.')
else:
    print('Você consegue o empréstimo!')