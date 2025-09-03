#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite seu sexo hihihihi [M/F]: ")).strip().upper()[0]  

while sexo not in 'MmFf':     # "enquanto sexo não for nenhuma das letras dessa palavra"
    print("Você digitou um sexo invalido seu... NAO BINARIO!!!")
    sexo = str(input("Digite seu sexo novemente [M/F]: ")).strip().upper()[0]

print("agora sim :D")

