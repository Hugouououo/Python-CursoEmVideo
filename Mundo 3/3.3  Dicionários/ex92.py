# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
anoAtual = date.today().year
dic = {}

# dic['nome'] = str(input('1. Digite o nome do funcionário: '))         inutil
dic['ano'] = int(input('2. Digite seu ano de nascimento: '))
dic['carteira'] = int(input('3. Digite o nº da carteira de trabalho [0 = Não possui]: '))
if dic['carteira'] != 0:
    dic['contratação'] = int(input('4. Digite o ano de contratação: '))
    # dic['salário'] = int(input('5. Digite o salário: '))
    
idade = anoAtual - dic['ano']
    
contribuição = anoAtual - dic['contratação'] 
aposentadoria = ( 30 - contribuição ) + idade

if idade > 60 or aposentadoria > 60:
    print(f'Você tem {idade} anos de idade e {contribuição} anos de contribuição, então já pode se aposentar.')
else:
    print(f'Sua contribuição é de {contribuição} anos.') 
    print(f'Você se aposentará com {aposentadoria} anos ou com 60 anos de idade.')
    

