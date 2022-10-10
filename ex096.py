def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno com {larg} X {comp} é de {a}m².')


print(' CONTROLE DE TERRENOS ')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento: '))
area(l, c)