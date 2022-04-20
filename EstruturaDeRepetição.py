for c in range(0, 6):
    print("Oi")
print('Fim')

#escreve de trás para frente
for c in range(7, 0, -1):
    print(c)
print("Fim")

#escreve de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('Fim')


n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

#soma com for
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores é {}'.format(s))

