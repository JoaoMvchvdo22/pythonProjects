salario = float(input('Qual o salário do Funcionário? R$ '))
porcentagem = salario*15/100
salReajuste = salario + porcentagem


print('O salário de R${:.2f} com o reajuste de 15% foi para R${:.2f}'.format(salario, salReajuste))

