s = float(input('Entre com o salário de um funcionário: '))

if s > 1250.00:
    print('Aumento de {}'.format(s+(s*0.10)))
else:
    print('Aumento de {}'.format(s+(s*0.15)))