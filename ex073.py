times = ('Palmeiras', 'Corinthians', 'Fluminense', 'AthleticoPR',
      'AtleticoMG', 'Internacional', 'Flamengo', 'Bragantino',
      'Santos', 'São Paulo', 'Ceará', 'Botafogo', 'Avaí', 'Goiás',
      'Cuiabá', 'Coritiba', 'AméricaMG', 'AtléticoGo', 'Fortaleza', 'Juventude')
print('-=' * 15)
print(f' Times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética são: {sorted(times)}')
print('-=' * 15)
print(f'o Coritiba está na {times.index("Coritiba")+1} posição')


