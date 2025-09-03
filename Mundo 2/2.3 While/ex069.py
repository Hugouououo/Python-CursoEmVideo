#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:                                                                               A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

homem = mulher = nda = 0 
maior = menor = 0
c = 1

while True:
    print(f'----- {c}ª pessoa -----')
    
    id = int(input('Idade: '))
    sx = str(input('Gênero [m/f/nda]: ')).lower().strip()[0] #primeira letra
    loop = str(input('Deseja continuar? [s/n]: ')).lower().strip()[0]
    
    # Idade
    if id < 18 and id > 0:
        menor += 1
    elif id >= 18:
        maior += 1
    else:
        print('* Idade Inválida, não será contada no resultado final. *')
        
    # Sexo
    if sx == 'm':
        homem += 1
    elif sx == 'f':
        mulher += 1
    elif sx == 'n':
        nda += 1
    else:
        print('* Gênero inválido (pro programa), não será contado no resultado final. *')

    # Fim do loop
    if loop == 'n':
        break
    elif loop == 's':
        c += 1
    else:
        print('* Resposta inválida, encerrando o registro. *')
        break

print('-'*50)
print(f'''Você registrou:
      - {mulher} mulheres
      - {homem} homens
      - {nda} pessoas que se identificam com outros gêneros''')
print(f'''Além disso, foram registradas {maior} pessoas maiores e {menor} menores de idade''')
print('-'*16, 'Fim do programa', '-'*17)