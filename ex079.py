números = list()
while True:
    num = int(input('Digite um número: '))
    if num not in números:
        números.append(num)
        print('Valhor adicionado com sucesso...')
    else:
        print('Valor duplicado, não adicionado...')
    escolha = str(input('Deseja coninuar? [Y/N]: ')).upper().strip()
    if escolha == 'N':
        break
números.sort()
print(f'Voce digitou os valores {números}')



