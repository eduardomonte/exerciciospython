frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#alternativa para python
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto [letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
