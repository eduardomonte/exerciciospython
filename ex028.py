'''import random
numero = int(input('Digite um númeto de 1 a 5 que voce acha que será escolhido pelo computador: '))
n = random.randint(1,5)
print('o número gerado foi {}'.format(n))
if n == numero:
    print('parabés, voce acertou!!!')
else:
    print('não foi dessa vez')'''

from random import randint
from time import sleep
computador = randint(0,5)
print('\033[1;32m-=-'*20)
print('\033[1;34mVou pensar em um número de 0 a 5. Tente advinhar...\033[m')
print('\033[1;32m-=-\033[m'*20)
jogador = int(input('\033[1;34mEm que número pensei?: '))
print('PROCESSANDO....')
sleep(3)
if jogador == computador:
    print('\033[1;32;44mPARABÉNS! VOCê CONSEGUIU ME VENCER!!!!!!!\033[m')
else:
    print('\033[1;31;40mGANHEI!!! Eu pensei no número {} e não no {}!\033[m'.format(computador, jogador))




