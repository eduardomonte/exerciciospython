d = int(input('quantos dias alugados?: '))
km = float(input('quantos quilometros foram rodados?: '))
b = (d*60) + (km*0.15)

print('o total a pagar é R${:.2f}'.format(b))