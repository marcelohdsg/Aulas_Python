# variáveis
hc = 0
m18 = 0
mm20 = 0
i = 0

#while principal
while True:

    i = int(input('Idade: '))
    s = ' '
    cadas = ' '
    #tratativa sexo
    while s not in 'MF':
        s = (input('Sexo [M/F]: ').strip().upper()[0])
    #atribuições
    if s == 'M':
        hc += 1
    if i > 18:
        m18 += 1
    if s == 'F' and i < 20:
        mm20 += 1
    #tratativa continuidade
    while cadas not in 'SN':
        cadas = input('\nCadastrar outro usuário? [S/N] ').strip().upper()[0]
    #mostrando dados
    if cadas == 'N':
        print(f'\nMaiores de 18: {m18}\n'
              f'Homens cadastrados: {hc}\n'
              f'Mulheres com menos de 20 anos: {mm20}')
        break




