v = float(input('Digite a velocidade do carro: '))
max = 100
cores = {'limpa':'\033[m',
        'vermelho':'\033[31m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
if v > 100:
    print('{}MULTADO! Voce excedeu o limite de 100 km/h, voce deve pagar multa de{}'.format(cores['vermelho'], cores['limpa']))
    multa = (v-100) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores['amarelo'],cores['limpa']))