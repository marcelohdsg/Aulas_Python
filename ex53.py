from random import randint

lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print ('Os valores sorteados foram: ', end='')
for cont in range(len(lista)):
    print(f'{lista[cont]}', end=' ')

print(f'\nO maior valor é: {max(lista)}')
print(f'O menor valor é: {min(lista)}')

