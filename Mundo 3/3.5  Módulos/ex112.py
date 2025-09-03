# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
# ---> Não consegui fazer o ex111, então tô usando tudo do moeda110:

def resumo(preço = 0, aum = 10, dim = 10):
    if preço.isalpha():
        print(f'ERRO: "{preço}" não é um preço válido')
    else:
        preço = preço.replace(',' , '.')
        preço = float(preço)
        # Código normal:
        print('---------- RESUMO DO VALOR ----------')
        print(f'Com um aumento de {aum}%, temos {format(aumentar(preço, aum))}')
        print(f'Com um desconto de {dim}%, temos {format(diminuir(preço, dim))}')
        print(f'O dobro de {format(preço)} é {format(dobro(preço))}')
        print(f'A metade de {format(preço)} é {format(metade(preço))}')


def aumentar(preço = 0, aum = 0):
    
    result = preço + preço * (aum / 100)
    return result
    

def diminuir(preço = 0, dim = 0):
    
    result = preço - preço * (dim / 100)
    return result

    
def dobro(preço = 0):
    return preço * 2


def metade(preço = 0):
    return preço / 2
    

def format(preço = 0, moeda = 'R$'):
    
    return f'{moeda}{preço :.2f}'.replace(',' , '.')