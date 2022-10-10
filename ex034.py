salario = float(input('Digite o valor do salário: '))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario *10 / 100)
print('Quem ganha o salário de R${:.2f} passará a receber R${:.2f}'.format(salario, novo))
