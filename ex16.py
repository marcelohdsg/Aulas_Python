##Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
##tangente desse ângulo.
from math import radians, sin, cos, tan

a = float(input('Entre com o ângulo: '))

print('O valor do SENO é: {:.2f}\n'
      'O valor do COSSENO é: {:.2f}\n'
      'O valor da TANGENTE é: {:.2f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))
