a = int(input("Ano de nascimento: "))
a = 2018 - a

if a < 18:
    print('Ainda vai se alistar.')
    print('Ainda faltam {} anos para o alistamento'.format(-a+18))
elif a == 18:
    print('Está na hora de se alistar.')
    print('Por favor, se aliste!')
else:
    print('Passou do tempo de se alistar')
    print('Vc está {} anos atrasado'.format(a-18))

