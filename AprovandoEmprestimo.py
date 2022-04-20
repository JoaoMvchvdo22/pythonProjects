valorCasa = int(input('Qual o valor da casa? R$'))
salario = int(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
valorPrestacao = (valorCasa / anos) / 12

print('Para pagar R${:.2f} em {} anos a prestação será de R${:.2f} por mês'.format(valorCasa, anos, valorPrestacao))

if valorPrestacao <= salario * 30/100:
    print('Empréstimo APROVADO!!!')
else:
    print('Empréstimo negado')
    