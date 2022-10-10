aluno = dict()
aluno['nome'] = str(input('Digite um nome: '))
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('=-'*30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')


'''pessoas = {'nome': 'Eduardo', 'sexo': 'M', 'Idade': 29}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')'''