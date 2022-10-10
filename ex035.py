print('-=-'*20)
print('                 ANALISANDOR DE TRIANGULOS                      ')
print('-=-'*20)
reta1 = float(input('Digite a reta 1: '))
reta2 = float(input('Digite a reta 2: '))
reta3 = float(input('Digite a reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os seguimentos acima PODEM FORMAR UM TRIANGULO')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIANGULO')
