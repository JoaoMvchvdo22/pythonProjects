import random
import time

print('Estou pensando em um número entre 0 e 10 \nserá que você consegue adivinhar?')
palpite = int(input('Qual o seu palpite? '))
computador = random.randint(0, 10)

print('PROCESSANDO...')
time.sleep(3)

