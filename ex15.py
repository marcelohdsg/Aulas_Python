##Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calculo e mostre o
##comprimento da hipotenusa

import math

co = float(input('Entre com o cateto oposto: '))
ca = float(input('Entre com o cateto adjacente: '))

print('A hipotenusa é: {}'.format(int(math.hypot(co, ca))))




