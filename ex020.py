import random
aluno1 = str(input('digite o nome do aluno 1: '))
aluno2 = str(input('digite o nome do aluno 2: '))
aluno3 = str(input('digite o nome do aluno 3: '))
aluno4 = str(input('digite o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)