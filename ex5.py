## Faça um programa que leia um número int e mostre na tela o seu sucessor e seu antecessor

n = int(input('Entre com um número: '))

print ('O sucessor do número digitado é: {} \n'
       'O antecessor do número digitado é: {}' .format(n+1, n-1))