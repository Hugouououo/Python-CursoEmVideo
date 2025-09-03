#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input("distancia da viagem em km: "))

if dist < 200 and dist > 0:
    print("sua viagem deu R${:.2f} no total.".format(dist * 0.50))
elif dist >= 200:                                                   #:.2 == dois zeros depois do preço
    print("sua viagem deu R${:.2f} no total.".format(dist * 0.45))
else:
    print("erro?")