nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')

#transforma totas as letras em maiúsculas
print('Seu nome em maúsculas é {}'.format(nome.upper()))

#tranforma todas as letras em minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

#informa quantas letras tem, retirando os espaços existêntes
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

print('Seu primeiro nome é {} e tem {} letras'.format(nome[:8], nome.find(' ')))





