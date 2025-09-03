#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Digite sua cidade: ')).strip() #elimina qualquer espaço antes

#print(bool(cid.count('sant')))
print('Sua cidade tem santo no nome: {}'.format(cid[:5].lower() == 'santo'))