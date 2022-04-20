dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km foram rodados? '))
pago = (dias*60) + (km*0.15)

print('O total a pagar é de R$ {:.2f}'.format(pago))

