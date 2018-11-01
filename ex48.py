from random import randint

titulo = 'JOGO DE PAR OU ÍMPAR'
print(f' ----------------- \n{titulo}\n -----------------')

while True:
    pi = input('\nPar ou Ímpar? [P/I] ')
    num = int(input('Qual o valor? '))

    c = randint(0, 5)
    v = (c + num)%2

    if pi == 'I' and v == 0:
        print(f'O computador mostrou {c} e você mostrou {num}. VOCÊ PERDEU!')
        break

    if pi == 'P' and v != 0:
        print(f'O computador mostrou {c} e você mostrou {num}. VOCÊ PERDEU!')
        break

    else:
        print(f'O computador mostrou {c} e você mostrou {num}. VOCÊ VENCEU!')





