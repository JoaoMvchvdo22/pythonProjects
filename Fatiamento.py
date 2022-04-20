#fatiamento usando números (tem que tranformar em string)
n = float(input('Digite um número qualquer: '))
numInt = str(n)

print('O número {} tem sua parte inteira {}'.format(n, numInt[0]))

#fatiamento usando string
frase = 'Olá Mundo, estou aprendendo Python'
print(frase[7])

#fatia do caractere 7 ao 20 (o 21 é excluído)
print(frase[7:21])

#fatia do caractere 7 ao 20 pulando de 2 em 2
print(frase[7:21:2])

#fatia do caractere 0 ao 6
print(frase[:7])

#fatia do caractere 7 e vai até final pulando de 3 em 3
print(frase[7::3])










