print('=' * 30)
print('            BANCO')
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))

while True:

    sobra = valor%50
    cinq = int((valor-sobra))/50

    sobrav = sobra%20
    vint = int((sobra-sobrav))/20

    sobrad = sobrav % 10
    cinc = int((sobrav - sobrad)) / 10

    sobrau = sobrad % 1
    um = int((sobrad - sobrau)) / 1

    if cinq > 0:
        print(f'Total de {cinq:.0f} cédulas de R$50')
    if vint > 0:
        print(f'Total de {vint:.0f} cédulas de R$20')
    if cinc > 0:
        print(f'Total de {cinc:.0f} cédulas de R$10')
    if um > 0:
        print(f'Total de {um:.0f} cédulas de R$1')

        print('\nVolte sempre!')

    break