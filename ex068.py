from random import randint
v = 0
print('=-='*10)
print('\033[34mVAMOS JOGAR PAR OU IMPAR...\033[m')
print('=-='*10)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    print('Vamos jogar novamente....')
print(f'Game over! Voce venceu {v} vezes')