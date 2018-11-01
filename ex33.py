n1 = float(input('Entre com o 1º número: '))
n2 = float(input('Entre com o 2º número: '))
n3 = float(input('Entre com o 3º número: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        maior = n1
        medio = n2
        menor = n3
    else:
        maior = n1
        medio = n3
        menor = n2

if n2 > n1 and n1 > n3:
    if n1 > n3:
        maior = n2
        medio = n1
        menor = n3
    else:
        maior = n2
        medio = n3
        menor = n1

if n3 > n1 and n3 > n2:
    if n2 > n1:
        maior = n3
        medio = n2
        menor = n1
    else:
        maior = n3
        medio = n1
        menor = n2

print('Maior número é {}\n'
      'Do meio é {}\n'
      'Menor é {}'.format(maior, medio, menor))


