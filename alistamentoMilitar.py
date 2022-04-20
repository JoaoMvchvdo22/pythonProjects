import datetime

anoAtual = datetime.date.today().year
nasc = int(input('Ano de nascimento: '))
idade = anoAtual - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, anoAtual))

if idade == 18:
    print('Voçê tem que se alistar esse ano!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não completou 18 anos, volte daqui {} anos para se alistar'.format(saldo))
    ano = anoAtual + saldo
    print('Seu ano de alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
    ano = anoAtual - saldo
    print('Seu ano de alistamento foi em {}'.format(ano))
