nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('seu nome em maísculas é: {}'.format(nome.upper()))
print('seu nome em minúsculas é: {}'.format(nome.lower()))
print('seu nome tem {} letras ao todo'.format(len(nome)-nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))