import random
aluno1 = str(input('digite o nome do 1 aluno: '))
aluno2 = str(input('digite o nome do 2 aluno: '))
aluno3 = str(input('digite o nome do 3 aluno: '))
aluno4 = str(input('digite o nome do 4 aluno: '))
aluno5 = str(input('digite o nome do 5 aluno: '))
lista = [aluno1,aluno2, aluno3, aluno4, aluno5]
sorteio = random.choice(lista)
print('o aluno sorteado foi {}'.format(sorteio))