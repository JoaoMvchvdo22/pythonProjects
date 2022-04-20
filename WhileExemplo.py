c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')

print('='*30)

n = 1
while n != 0:
    n = int(input('Digite um valor:'))
print('Fim!!')

print('='*30)

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? ')).strip().upper()[0]
print('FIM!')

print('='*30)

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} números pares e {} números ímpares'.format(par, impar))
