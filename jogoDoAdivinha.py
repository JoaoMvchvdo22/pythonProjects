import random
import time

num = int(input('Tente adivinhar o número que estou pensando de 0 a 5: '))
computador = random.randint(0, 5)#Faz o computador randomizar algo

print('PROCESSANDO...')
time.sleep(3)#espera alguns segundos para executar a proxima ação

if num == computador:
    print('Você acertou, eu estava pensando no número {}'.format(num))
else:
    print('Você errou :(, eu estava pensando no número {}'.format(computador))
