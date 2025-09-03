#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

preço = float(input("digite o preço: "))

metodo = int(input("""Digite o método de pagamento:
    1 = à vista dinheiro/cheque: 10porcento de desconto
    2 = à vista no cartão: 5porcento de desconto
    3 = em até 2x no cartão: preço formal 
    4 = 3x ou mais no cartão: 20porcento de juros
    """))

if metodo == 1:
    print(preço * 0.90)
elif metodo == 2:
    print(preço * 0.95)
elif metodo == 3:
    print(preço)
elif metodo == 4:
    print(preço * 1.20)
else:
    print("erro")