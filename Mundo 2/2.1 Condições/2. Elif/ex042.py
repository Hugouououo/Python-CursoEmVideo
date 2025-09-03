# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

l1 = int(input("lado 1: "))
l2 = int(input("lado 2: "))
l3 = int(input("lado 3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1: 
    print("da pra formar triangulo:")                                       
    if l1 == l2 == l3:                                                            
        print("EQUILATERO")                                                      
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print("ISOCELES")
    elif l1 != l2 != l3 and l1 != l3 != l2 and l2 != l3 != l1:
        print("ESCALENO")
    else:
        print("erro?????")
else:
    print("não dá pra formar triangulo")


#compliquei demais. era mais facil do jeito do guanabara
#https://youtu.be/ZX7sCPjcHA0?si=lgkNMmtPUHN7Po9I&t=686