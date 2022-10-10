n = cont = soma = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    soma = soma + n
    cont += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))

print('Voce digitou {} números, e a soma foi {}.'.format(cont, soma))

