nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4.9:
    print('\033[1;31mAluno REPROVADO!!!\033[m')
elif media >= 5 and media <= 6.9:
    print('\033[1;33mALUNO EM RECUPERAÇÃO!!!\033[m')
elif media >= 7.0:
    print('\033[1;32mALUNO APROVADO!!!\033[m')