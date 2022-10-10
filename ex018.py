import math
valor = float(input('digite um angulo que voce deseja: '))
seno = math.sin(math.radians(valor))
cos = math.cos(math.radians(valor))
tang = math.tan(math.radians(valor))
print('O angulo de {} tem o seno {:.2f} \n o angulo de {} tem Cosseno de {:.2f} \n o angulo de {} tem tangente {:.2f}'.format(valor, seno, valor, cos, valor, tang))