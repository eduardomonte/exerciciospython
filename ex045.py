from  random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
cumputador = randint(0, 2)
print(''' Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO!!!')
sleep(1)
print('KEN!!!')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 10)
print ('O computador escolheu {}'.format(itens[cumputador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=' * 10)
if cumputador == 0:
    if jogador == 0:
        print('JOGO EMPATADO')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')
elif cumputador == 1:
    if jogador == 0:
        print(' COMPUTADOR VENCE')
    elif jogador == 1:
        print('JOGO EMPATADO')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida')

elif cumputador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGO EMPATADO')
    else:
        print('Jogada inválida')
