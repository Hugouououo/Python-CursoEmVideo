def aumentar(preço = 0, taxa = 0):
    
    result = preço + preço * (taxa / 100)
    return result
    

def diminuir(preço = 0, taxa = 0):
    
    result = preço - preço * (taxa / 100)
    return result

    
def dobro(preço = 0):
    return preço * 2


def metade(preço = 0):
    return preço / 2
    

# EX 108 
def format(preço = 0, moeda = 'R$'):
    
    return f'{moeda}{preço :.2f}'.replace(',' , '.')