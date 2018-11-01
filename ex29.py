v = float(input('Qual a velocidade do carro?: '))

if v > 80:
    m = v - 80
    print('Você foi multado em {} Reais.'.format(m*7.00))
else:
    print('Sem multa!')
