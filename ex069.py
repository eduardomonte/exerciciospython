totalman = maioridade = mulher20 =0
while True:
    print('-=' * 10)
    nome = str(input('Digite o nome: ')).upper()
    sexo = str(input('Sexo [M/F]: ')).upper()
    idade = int(input('Digite a Idade: '))
    usuario = str(input('Deseja continuar? [Y/N]: ')).strip().upper()[0]
    print('-=' * 10)
    if sexo == 'M':
       totalman += 1
    if idade >= 18:
        maioridade += 1
    if sexo == 'F' and idade <= 20:
        mulher20 += 1
    if usuario == 'N':
        break

print('Fim do programa...')
print(f'Fora cadastrados {totalman} homemns.')
print(f'Foram cadastradas {maioridade} pessoas maiores de idade.')
print(f'Foram cadastradas {mulher20} mulheres abaixo dos 20 anos de idade.')
