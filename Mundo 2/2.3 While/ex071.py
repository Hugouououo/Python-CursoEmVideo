# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.  OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*5, 'Super Banco ou algo assim', '='*6)
    
saque = int(input('Valor a ser sacado: '))
dinheiro = saque
ced = 50
totCed = 0

print('Você recebeu: ')
while True:
    
    if dinheiro >= ced:
        dinheiro = dinheiro - ced
        totCed += 1
        
    else:
        if totCed > 1:
            print(f'- {totCed} cédulas de R${ced}')
        elif totCed == 1:
            print(f'- {totCed} cédula de Rs{ced}')
            
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        
        if dinheiro == 0:
            break
        
print('='*38)