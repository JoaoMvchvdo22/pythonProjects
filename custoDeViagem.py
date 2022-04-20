distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('A sua viagem vai custar R${:.2f}'.format(preco))

