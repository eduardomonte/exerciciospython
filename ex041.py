from datetime import date
atual = date.today().year
nas = int(input('Digite o ano de nascimento: '))
idade = atual - nas
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('o atleta é MIRIM')
elif idade <= 14:
    print('o atleta é INFANTIL')
elif idade <= 19:
    print('o atleta é JÙNIOR')
elif idade <= 25:
    print('o atleta é SENIOR')
elif idade >= 26:
    print('o atleta é MASTER')