#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

comp = randint(0,10)
jog = int(input("Escolha um número de 0 a 10 e veja se é igual à escolha do computador: "))
palp = 0

while jog != comp:
    if jog >= 0 and jog <= 10:
        if jog < comp:
            print("Você errou, tente um número maior...")
            jog = int(input("Escolha um número de 0 a 10 e veja se é igual à escolha do computador: "))
            palp += 1
        elif jog > comp:
            print("Você errou, tente um número menor...")
            jog = int(input("Escolha um número de 0 a 10 e veja se é igual à escolha do computador: "))
            palp += 1
    else:
        print("Número invalido!!!!")

print("Acerto miseravi")
print("(Com {} palpites  ',:| )".format(palp+1))