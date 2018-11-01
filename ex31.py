v = float(input('Qual a distância da viagem em KM?: '))

if v < 200:
    print('O valor da viagem é {} Reais'.format(v*0.50))
else:
    print('O valor da viagem é {} Reais'.format(v*0.45))