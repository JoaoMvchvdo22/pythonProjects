soma = 0
cont = 0
for c in range(1, 7,):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 3 == 0:
        soma += num
        cont += 1
print('A soma dos {} valores pares é {}'.format(cont, soma))
