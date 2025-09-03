# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: 
# A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
#cinco = 'Não.'

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    
    # Jeito bem burro de fazer:
    # if n == 5:   
    #     cinco = 'Sim!'
        
    cont = str(input('Deseja continuar? [s/n]: '))
    if cont not in 'SSss':
        break  # melhor do que "in 'NNnn' pq se digitar um outro número tbm encerra

print(f'--- Sua lista: {lista} ---')

print(f'A) Quant. de números: {len(lista)}')

lista.sort(reverse=True) # se for a declaração de uma var. retorna "None"
print(f'B) Lista ordenada de modo decrescente: {lista}')


# Jeito bem burro de fazer:
# print(f'C) O Valor 5 está na lista?: {cinco}')
# Jeito certo: 
if 5 in lista:
    print('C) O valor 5 está na lista!')
else:
    print('C) O valor 5 não está na lista.')
