#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

total = []
aluno = 0

while True:
    
    total.append([[],[],[]])

    total[aluno][0] = str(input('nome '))
    total[aluno][1] = float(input('nota1 '))
    total[aluno][2] = float(input('nota2 '))
    aluno+=1
    
    cont = input('continuar? [s/n] ')
    if cont not in 'SSss':
        break
    
print('--- Médias ---')
for c in range(aluno):
    
    media = float( ( total[c][1] + total[c][2] ) / 2 )
    print(f'{c}. {total[c][0]}: {media} ')
    

verNotas = input('Gostaria de ver as notas de algum aluno? [s/n]: ')
while verNotas in 'SSss':
    
    a = int(input('Qual aluno? (baseado no nº do boletim): '))
    
    print(f'| Aluno: {total[a][0]} | notas: {total[a][1]} , {total[a][2]} |')
    
    verNotas = input('Gostaria de ver as notas de outro aluno? [s/n]: ')

print('Programa encerrado...')