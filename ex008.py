d = float(input('uma distancia em metros: '))
print('a medida de {}, corresponde a: '.format(d))
km = d/1000
hm = d/100
dam = d/10
dm = d*10
cm = d*100
mm = d*1000
print(km,'km', hm, 'hm', dam, 'dam', dm, 'dm', cm, 'cm')

#print('a medida de {}m corresponde a {:,0f}cm e {:.0f}mm'.format(medida, cm, mm))