valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if resposta in 'N':
        break
print('=-'*30)
print(f'Voce digitou {len(valores)} elementos')
print('=-'*30)
valores.sort(reverse=True)
print(f'Os Valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')