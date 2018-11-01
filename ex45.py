from random import randint

c = int(input('''\nVAMOS JOGAR!! 
1 - PEDRA
2 - PAPEL
3 - TESOURA 

Qual a sua escolha? '''))

if c == 1:
    c = 'PEDRA'
elif c == 2:
    c = 'PAPEL'
else:
    c = 'TESOURA'

pc = randint(1, 3)
if pc == 1:
    pc = 'PEDRA'
elif pc == 2:
    pc = 'PAPEL'
else:
    pc = 'TESOURA'

if (c == 'PEDRA' and pc == 'TESOURA') or\
   (c == 'PAPEL' and pc == 'PEDRA') or\
   (c == 'TESOURA' and pc == 'PAPEL'):

    print('''
    COMPUTADOR: {}
    VOCÊ: {} 

    VOCÊ VENCEU!'''.format(pc, c))

elif c == pc:
    print('''
        COMPUTADOR: {}
        VOCÊ: {} 

        DEU EMPATE!'''.format(pc, c))

else:
    print('''
    COMPUTADOR: {}
    VOCÊ: {} 

    VOCÊ PERDEU!'''.format(pc, c))