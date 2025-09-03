#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("digite seu salario: "))

if sal <= 1250:
    print("aumento de 15:")
    print("{:.2f}".format(sal * 1.15)) #15% a mais
else:
    print("aumento de 10%:")
    print("{:.2f}".format(sal * 1.10))