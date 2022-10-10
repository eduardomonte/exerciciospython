a = int(input('Digite o nº1: '))
b = int(input('Digite o nº2: '))
c = int(input('Digite o nº3: '))
#testando o menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado {}'.format(menor))
print('O maior valor digitado {}'.format(maior))
