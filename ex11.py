## Faça um prog que leia a largura e a altura de uma parede em metros, calcule a sua área, e a quantidade de tinta
## necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

n1 = float(input('Entre com a ALTURA da parede em metros: '))
n2 = float(input('Entre com a LARGURA da parede em metros: '))

a = (n1*n2)

print('\nA área da parede é {} m²! \n'
      'Sendo assim, será(ão) necessário(s) {} litro(s) de tinta.'.format(a, a/2))


