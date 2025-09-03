#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

pes = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))

imc = pes / alt**2

if imc <= 18.5:
    print('Seu imc é {}, logo, você está: {}'.format(imc, 'Abaixo do peso'))
elif imc > 18.5 and imc <= 25:
    print('Seu imc é {}, logo, você está no: {}'.format(imc, 'Peso ideal'))
elif imc > 25 and imc <= 30:
    print('Seu imc é {}, logo, você está com: {}'.format(imc, "Sobrepeso"))
elif imc > 30 and imc <= 40:
    print('Seu imc é {}, logo, você está com: {}'.format(imc, 'Obesidade'))
elif imc > 40:
    print('Seu imc é {}, logo, você está com: {}'.format(imc, "Obesidade Mórbida"))