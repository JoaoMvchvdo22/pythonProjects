sexo = str(input('informe o seu sexo: ')).strip().upper()[0]

#enquanto a variável "sexo" não receber M, m ou F, f. Continua perguntando
while sexo not in 'M ou F':
    sexo = str(input('Sexo inválido, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
