#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Digite a velocidade do carro: '))

if v > 80:
    print('Acima da velocidade permitida!')
    print('Sua multa é de: R${},00'.format((v - 80) * 7))

else: 
    print('Continue assim!')