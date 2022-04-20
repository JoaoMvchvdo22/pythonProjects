nome = input('Aluno: ')
n1 = float(input('Nota da P1: '))
n2 = float(input('Nota da P2: '))
n3 = float(input('Nota de participação: '))
n4 = float(input('Nota dos exercícios: '))
s = n1 + n2 + n3 + n4
d = s / 4
print('Total de pontos: {}'.format(s))
print('Média final: {}'.format(d))
