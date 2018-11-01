vp = float(input('Valor pago: '))
c = int(input('''\nMENU:
1 - À VISTA
2 - À VISTA NO CARTÃO
3 - 2X NO CARTÃO 
4 - 3X OU MAIS NO CARTÃO

Condição de pagamento: '''))

if c == 1:
    print('Valor a se pagar: {:.2f}'.format(vp - (vp * 0.10)))
elif c == 2:
    print('Valor a se pagar: {:.2f}'.format(vp - (vp * 0.05)))
elif c == 3:
    print('Valor a se pagar: {:.2f}'.format(vp))
else:
    print('Valor a se pagar: {:.2f}'.format(vp + (vp * 0.20)))