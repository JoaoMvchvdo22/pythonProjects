vel = int(input('Qual velocidade o carro passou? '))
multa = (vel-80) * 7

if vel > 80:
    print('Vá com calma o limite da via é 80km/h, você passou à {}km/h'.format(vel))
    print('Deverá pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia!')
