## Faça um programa que leia um número qualquer, e mostre na tela a sua tabuada. 

n = int(input('Entre com um número: '))

c = 0
while (c < 10):
    print('{} x {} = {}'.format(c, n, c*n))
    c = c+1