l = float(input('digite a largura da parede: '))
a = float(input('digite a altura da parede: '))
área = l*a
print('Sua parede possui dimensões de {}x{} e sua área é de {}m²'.format(l, a, área))
tinta = área / 2
print('serão necessários {}L de tintas'.format(tinta))