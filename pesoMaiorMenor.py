maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa mais pesada tem {} kg'.format(maior))
print('E a pessoa mais leve tem {} kg'.format(menor))

