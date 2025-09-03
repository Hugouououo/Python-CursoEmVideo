#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Digite sua idade: '))

if idade == 18:
    print('Você já pode se alistar no serviço militar!')
elif idade > 18:
    print('Você já devia ter se alistado no serviço militar aos 18 anos.')
elif idade < 18:  #else funcionaria do mesmo jeito
    print('Você ainda não pode se alistar no serviço militar, a inscrição é aos 18 anos. Faltam {} anos para você poder se alistar.'.format(18-idade))