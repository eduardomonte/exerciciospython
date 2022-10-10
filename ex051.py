print('='*40)
print('       OS DEZ TERMOS DE UMA PA      ')
print('='*40)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for c in range (termo,decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU!')