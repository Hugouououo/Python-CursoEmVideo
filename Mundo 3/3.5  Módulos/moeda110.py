def resumo(preço = 0, aum = 10, dim = 10):
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