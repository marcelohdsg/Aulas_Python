ano = int(input('Entre com um ano: '))

if ano%4 == 0 and ano%100 != 0:
    print('O ano É BISSEXTO')
else:
    print('O ano NÃO É BISSEXTO')


