from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),
       randint(1,10), randint(1,10))
print(f'Os números gerados foram: ', end='')
for n in num:
    print(f' {n} ', end='')
print(f'\nO maior valor gerado foi {max(num)}')
print(f'O menor valor gerado foi {min(num)}')
