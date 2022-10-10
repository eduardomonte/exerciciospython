viagem = float(input('Digite quantos km é sua viagem: '))
if viagem <= 200:
   preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('O preço da sua passagem é de R${:.2f}'.format(preço))
