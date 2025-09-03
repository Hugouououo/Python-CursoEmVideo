#leia duas notas de um aluno e mostre a média

n1 = float(input('Digite sua nota da P1:'))
n2 = float(input('Digite sua nota da P2:'))

soma = n1 + n2
media = soma / 2

print('Sua média é: {:.1f}'.format(media))