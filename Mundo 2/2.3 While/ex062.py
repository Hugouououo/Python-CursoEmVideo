#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

t = int(input("digite o primeiro termo: "))
r = int(input("digite a razão: "))
c = 1

print(t)
while c <= 5:
    print(t * (r * c))
    c += 1 

m = int(input("ditite mais quantos termos gostaria: "))
while m != 0:    
    print(t)
    while c <= (5 + m):
        print(t * (r * c))              # erro
        c += 1 
    m = int(input("ditite mais quantos termos gostaria: "))
        