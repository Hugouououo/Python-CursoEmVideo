nome = str(input('Digite seu nome:'))

print('-'*40)
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' ')) #retira todos os espaços
primeiro = nome.split()
print(len(primeiro[0]))
print('-'*40)

#Crie um programa que leia o nome completo de uma pessoa e mostre:                        
# – O nome com todas as letras maiúsculas e minúsculas.                                     
# – Quantas letras ao todo (sem considerar espaços).                                        
# – Quantas letras tem o primeiro nome.
