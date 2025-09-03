# Crie um programa que leia dois valores e mostre um menu na tela. O programa deve realizar a operação em cada caso.  
#[ 1 ] somar    [ 2 ] multiplicar   [ 3 ] maior    [ 4 ] novos números    [ 5 ] sair do programa

n1 = int(input("n1"))
n2 = int(input('n2'))

x = int(input("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
 -> """))

while x != 5:
   
    if x == 1:
        print("{} + {} = {}".format(n1,n2, n1+n2))
        
    elif x == 2:
        print("{} x {} = {}".format(n1,n2, n1*n2))
        
    elif x == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1,n2))
        elif n2 < n1:
            print("{} é maior que {}".format(n2,n1))
        elif n1 == n2:
            print("os números são iguais")
        else:
            print("erro")                   # algo ta errado aqui

    elif x == 4:
        n1 = int(input("n1"))
        n2 = int(input('n2'))
    
    else:
        print("Número inválido")
        
    x= int(input("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
 -> """))

print("Fim do programa...")
