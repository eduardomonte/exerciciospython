total = totmil = menor = cont = 0
barato = ''
while True:
    print('=-'*10)
    print('LOJÃO BARATÃO DA PIROCA')
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:~^40}'.format(' Fim do programa! '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


