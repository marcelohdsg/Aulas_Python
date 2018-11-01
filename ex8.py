## Escreva um prog que leia um valor em metros, e converta ele em cm e mm

n = float(input('Digite um valor em metros: '))

print('O valor em centímetros é: {}\n'
      'O valor em milímetros é: {}'.format(int(n*100), int(n*1000)))
