import datetime
anoAtual = datetime.date.today().year
nasc = int(input('Ano de nascimento do atleta: '))
idade = anoAtual - nasc

print('O atleta tem {}'.format(idade))

if idade <= 9:
    print('Clasificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')