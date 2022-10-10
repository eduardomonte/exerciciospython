casa = float(input('Digite o valor do imível: '))
salario = float(input('Digite seu salário R$ '))
tempo = int(input('Em quantos anos quer pagar: '))
mensalidade = casa / (tempo*12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo), end='')
print(' a prestação será de R${:.2f}'.format(mensalidade))
if mensalidade <= minimo:
    print('Empréstimo pode ser CONCEDIDO!!')
else:
    print('Empréstimo NEGADO!')