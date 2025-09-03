# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, maior nota, menor nota, media da turma, situação (opcicional).
from math import ceil

def notas( * n, sit = False):
    r = {}
    r['Quantidade'] = len(n) 
    r['Maior'] = max(n)  # valor MÁXIMO de n
    r['Menor'] = min(n)  # valor MÍNIMO de n
    r['Média'] = ceil(sum(n) / len(n))  # arredonda pra cima
    
    if sit == True:
        if r['Média'] > 7:
            r['Situação'] = 'Boa'
        elif r['Média'] > 6:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    
    return r
        
resp = notas(10, 4.5, 1.5, sit=True)
print(resp)

