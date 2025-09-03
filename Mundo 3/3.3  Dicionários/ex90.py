# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média de {aluno['Nome']}: '))

if aluno['Média'] >= 7:
    #print(f'{aluno["nome"]} está aprovado(a)!')
    aluno['Situação'] = 'Aprovado'
else:
    #print(f'{aluno["nome"]} não foi aprovado(a).') 
    aluno['Situação'] = 'Reprovado'
    
print('-'*20)

for key, value in aluno.items():
    print(f'-> {key}: {value}.')
    