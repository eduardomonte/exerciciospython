temp = []
principal = []
maior = menor = 0

while True:
    temp.append(str(input('Digite um nome: ')))
    temp.append(float(input('Digite peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp [1] > maior:
            maior = temp[1]
        if temp [1] < menor:
            menor = temp [1]
    principal.append(temp[:])
    temp.clear()
    pergunta = str(input('Deseja prosseguir? [S/N]: ')).upper().strip()
    if pergunta == 'N':
        break
print(f'OS dados foram {principal}')
print('-='*30)
print(f'O maior peso encontrado foi de {maior} kg ', end='')
for p in principal:
    if p [1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso encontrado foi de {menor} kg. peso de ', end='')
for p in principal:
    if p [1] == menor:
        print(f'{p[0]} ', end='')
print()
print('-='*30)

'''for p in pessoas:
    if p >= 0:
        totmai += 1
    elif p in pessoas:
        if p <= totmai:
            totmen += 1

print(f'Ao todo foram cadastradas {pessoas}.')
print(f'O maior peso foi de {pessoas[:]} .')
print(f'TO menor peso foi de {pessoas[0]} .')'''