n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] BINARIO
[2] OCTAL
[3] HEXA''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igal a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual {}'.format(n, hex(n)[2:]))
else:
    print('opção inválida, tente novamente')
