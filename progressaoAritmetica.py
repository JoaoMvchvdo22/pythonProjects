primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao #fórmula do enésimo termo
for c in range(primeiro, decimo, razao):
    print(c, end=' ')
print('FIM!')