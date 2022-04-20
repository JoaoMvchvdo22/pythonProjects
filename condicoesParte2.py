nome = str(input('Qual seu nome? '))
if nome == 'João':
    print('Belo nome!')
elif nome == 'Vitor' or nome == 'Adriana':
    print('Nossa, é o nome dos meus pais!')
else:
    print('Ah sim!')
print('Tenha um bom dia, {}!'.format(nome))


