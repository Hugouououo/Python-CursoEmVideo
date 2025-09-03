def aumentar(preço = 0, taxa = 0):
    
    result = preço + preço * (taxa / 100)
    print(f'Com um aumento de {taxa}%, temos {result}')
    

def diminuir(preço = 0, taxa = 0):
    
    result = preço - preço * (taxa / 100)
    print(f'Com um desconto de {taxa}%, temos {result}')
    
    
def dobro(preço = 0):

    print(f'O dobro de {preço} é {preço*2}')


def metade(preço = 0):
    
    print(f'A metade de {preço} é {preço/2}')
    
