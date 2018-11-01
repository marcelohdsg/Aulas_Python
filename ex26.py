#Entre com uma frase e verifique as condições abaixo

f = input('Entre com uma frase: ')
f = f.upper()

print('A letra "A" aparece {} vezes.'.format(f.count('A')))
print('Ela aparece a primeira vez na {}º posição'.format(f.find('A')+1))
print('Ela aparece a última vez na {}º posição'.format(f.rfind('A')+1))
