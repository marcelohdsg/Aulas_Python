contagem = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', \
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', \
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', \
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', \
           'Dezenove', 'Vinte'

while True:

        num = int(input('Digite um número de 0 a 20: '))

        if num <= 20 and num > 0:
            print(f'O número digitado foi {contagem[num]}')
            break

        print('Errado!', end=' ')