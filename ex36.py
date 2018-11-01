v = float(input('Valor da casa: '))
s = float(input('Valor da salário: '))
a = float(input('Pagar em quantos anos? '))

p = v/(a*12)
print('Valor da parcela: {:.2f} '.format(p))

if p > (s*0.30):
    print('Infelizmente você não poderá comprar a casa. \n'
          'Total de {}% do salário'.format(int(p*100/s)))
