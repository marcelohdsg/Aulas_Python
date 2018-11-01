while True:
    n = (int(input('Qual tabuada você quer?: ')))
    s = 0
    if n < 0:
        print('Tabuada encerrada!')
        break

    while s < 11:
        print(f'{n} x {s} = {n*s}')
        s += 1






