## Crie um algoritmo que leia um número e mostre o seu dobro, triplo e o quadrado.

import math

n = int(input('Entre com um número: '))

print('O dobro do número é: {}\n'
      'O triplo do número é: {}\n'
      'A raíz quadrada é: {}'.format(n*2, n*3, int(math.sqrt(n)) ))
