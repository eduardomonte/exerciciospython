sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, formar o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

