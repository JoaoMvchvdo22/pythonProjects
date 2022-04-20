#verifica as primeiras letras de uma string
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')





#procura uma string dentro de outra
nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Machado? {} '.format('MACHADO' in nome.upper()))





#primeira e ultima ocorrencia de uma string
frase = str(input('Digite uma frase: ')).upper().strip()

#informa quantas vezes x letra aparece
print('A letra "A" aparece {} vezes'.format(frase.count('A')))

#informa a primeira posição que x letra apareceu
print('Ela aparece primeiro na posição {}'.format(frase.find('A')+1))

#informa a ultima posição que x letra apareceu
print('E aparece pela última vez na posição {}'.format(frase.rfind('A')+1))




nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))














