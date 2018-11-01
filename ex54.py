#lista ler do usuário

num = int(input('Entre com um número: ')), \
      int(input('Entre com um número: ')), \
      int(input('Entre com um número: ')), \
      int(input('Entre com um número: '))

#valores
print(f'\nVocê digitou os valores {num}')

#quantas x num 9
print(f'O número 9 apareceu {num.count(9)}x')

#número 3
if 3 in num:
    print(f'O número 3 aparece pela primeira vez na {num.index(3)+1}º posição')
else:
    print('O número 3 não existe na lista')
print(f'Os números pares são: ', end='')

#quais números pares
for i in range (len(num)):
    if num[i]%2 == 0:
        print(num[i], end=' ')




