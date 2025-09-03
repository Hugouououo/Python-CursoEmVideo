#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

verm = '\033[31m' ; verd = '\033[32m' ; azul = '\033[34m' ; reset = '\033[00m' # cores

exp = input('Digite sua expressão: ')

aberto = exp.count('(')
fechado = exp.count(')')

if '(' in exp:
    if aberto == fechado:
        print(f'{verd}Sua expressão está com todos os parênteses fechados. {reset}')
    else:
        print(f'{verm}Sua expressão não tem todos os parênteses fechados corretamente. {reset}')
else:
    print(f'{azul}Sua expressão não tem parênteses. {reset}')
    

# o guanabara fez colocando os parenteses que abrem numa lista e removendo-os quando encontrar os que fecham, se a lista ficar vazia é pq todos tão fechados