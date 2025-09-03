#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input("digite uma frase: ")).lower().replace(" ", "") # tira  e s p a ç o s  e deixa MAIUSCULO
print(frase)
esarf = frase[::-1] #esarf == frase ao contrário  :O

print(esarf)
if frase == esarf:
    print("PALÍNDROMO")
else:
    print("Não é PALÍNDROMO")
    
