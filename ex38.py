n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))

if n1 > n2:
    print('O PRIMEIRO valor é MAIOR')
elif n2 > n1:
    print('O SEGUNDO valor é MAIOR')
else:
    print('Não existe número maior, os dois são iguais')