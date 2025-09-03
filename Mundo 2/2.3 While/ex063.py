# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.    Ex: 0, 1 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8 [...]

n = int(input('Quantos termos quer? '))

n0 = 0 #primeiro termo
n1 = 1 #segundo termo
n2 = 0 #próximo termo
cont = 0

while cont < n:
    print('{} ->'.format(n2), end=' ') # end=' ' -> o print não dá enter durante as repetições
    n0 = n1   #o termo se torna seu sucessor
    n1 = n2   #o sucessor se torna seu sucessor       por exemplo: 1->2, 2->3, 2+3 ... 2->3, 3->4, 3+4
    n2 = n0 + n1   #ambos são somados               
    cont += 1
print('FIM')

#eu copiei esse código, agora eu sei o que é uma sequencia de fibonacci pelo menos, e entendi como funciona