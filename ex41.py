a = int(input('Ano de nascimento: '))
a = 2018 - a
if a < 9:
    print('MIRIM')
elif a < 15:
    print('INFANTIL')
elif a < 20:
    print('JUNIOR')
elif a < 21:
    print('SENIOR')
else:
    print('MASTER')
