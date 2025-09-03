# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.]

azul = '\033[34m' ; reset = '\033[0m'

ajuda = str(input('Digite o nome do comando que tem dúvidas sobre [digite FIM para encerrrar]: '))

while True:

    if ajuda == 'FIM':
        print('Volte sempre!')
        break
    else:
        print(f'{azul}{help(ajuda)}{reset}')
        print('-'*40)
        ajuda = str(input('Tem dúvida em algum outro comando?: '))
        
        



# só n funcionou a cor mas da pro gasto