larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
a = larg * alt
tinta = a / 2

print('Sua parede de {}x{} tem a área igual a {}m².'.format(larg, alt, a))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))


