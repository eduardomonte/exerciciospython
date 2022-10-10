print('{:=^40}'.format(' LOJAS MONTES '))
preço = float(input('Digite o valor das compras R$:  '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opção = int(input('Digite a opção desejada: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(' Sua compra parcelada em 2x de R$ {:.2f}, SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 /100)
    totparcelas = int(input('Digite o número de parcelas: '))
    parcela = total / totparcelas
    print('Sua compra será parcelada em {}x de R${:.2f}, COM JUROS'.format(totparcelas, parcela))
else:
    total = preço
    print('Opção inválida, tente novamente')
print('Sua compra no valor de R${:.2f} custará R${:.2f}'.format(preço, total))


