#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))
lista = [nome1,nome2,nome3,nome4]
#res = random.choice(lista) #Escolha aleatória dentro da Lista

print('-'*30)
print("O Aluno escolhido foi: {}".format(random.choice(lista)))
print('"'*30)