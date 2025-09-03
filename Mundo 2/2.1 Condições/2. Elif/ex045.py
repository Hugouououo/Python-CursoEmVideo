#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

escolhas = ('Pedra', 'Papel', "Tesoura") #0,1,2

computador = randint(0,2) #escolher de 0 a 2
jogador = int(input("""
                    0 = PEDRA
                    1 = PAPEL
                    2 = TESOURA
                    Faça sua escolha: """))

print("Sua escolha foi: {}".format(escolhas[jogador]))
print("A escolha do computador foi: {}".format(escolhas[computador]))

