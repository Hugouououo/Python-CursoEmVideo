#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

atual = 2024
totalMaior = 0
totalMenor = 0

for pessoa in range(1, 8):
    
    nasc = int(input("Em que ano a {}ª pessoa nasceu?".format(pessoa)))
    idade = atual - nasc
    
    print("(Essa pessoa tem {} anos de idade)".format(idade))
    
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
        
print("Das 7 pessoas, {} são maiores de idade e {} são menores.".format(totalMaior, totalMenor))
    