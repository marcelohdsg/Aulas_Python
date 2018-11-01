n = int(input('Entre com um número: '))

b = int(input('''Levando em consideração o menu abaixo: '
1 = Binária'
2 = Octal'
3 = Hexa
Escolha a base de conversão: '''))

if b == 1:
    print(bin(n)[2:])
elif b == 2:
    print(oct(n)[2:])
elif b == 3:
    print(hex(n)[2:])
else:
    print('Opção inválida, tente novamente!')
