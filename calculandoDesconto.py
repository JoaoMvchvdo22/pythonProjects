preco = float(input('Qual o preço do produto? R$'))
porcentagem = preco*5/100
precoDesc = preco - porcentagem


print('O produto custava R${} e com o desconto de 5% está saindo por R${}.'.format(preco, precoDesc))
