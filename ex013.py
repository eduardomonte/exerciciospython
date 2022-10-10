s = float(input('digite o salário do funcionário R$: '))
a = s + (s*15/100)
print('o salário do funcionpario passará de R${:.2f}, para, com 15% de aumento, R${:.2f}'.format(s, a))