v1 = float(input('Entre com a primeira medida em cm: '))
v2 = float(input('Entre com a segunda medida em cm: '))
v3 = float(input('Entre com a terceira medida em cm: '))

if v1 < (v2 + v3) and v2 < (v1 + v3) and v3 < (v2 + v1):
    if v1 == v2 == v3:
        print("Equilátero")

    elif v1 != v2 != v3 != v1:
        print('Escaleno')

    else:
        print('Isósceles')

else:
    print('NÃO TRIANGULO')