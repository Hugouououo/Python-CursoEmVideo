# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto (ano=0):
    idade = 2024 - ano
    if idade >= 18 and idade < 60:
        return 'OBRIGATÓRIO'
    elif idade >= 16 and idade < 18 or idade > 60:
        return 'OPCIONAL'
    else:
        return 'NEGADO'
    
ano = int(input('Digite o ano de nascimento: '))
print(f'Você tem {2024 - ano} anos e seu voto é {voto(ano)}')
    