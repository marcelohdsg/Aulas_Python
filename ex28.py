from random import randint

n = randint(0,5)
num_dig = int(input('Tente adivinhar o numero... Digite um número de 0 a 5: '))

if num_dig == n:
    print('Você VENCEU!')
else:
    print('O computador venceu :(')
