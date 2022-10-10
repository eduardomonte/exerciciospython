p = float(input('digite o valor do produto R$: '))
d = p - (p*5/100)
print('preço do produto é R${:.2f}, na promoção com desconto de de 5% custará R${:.2f}'.format(p, d))