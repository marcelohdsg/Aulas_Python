lista = ['Pão', 1, 'Leite', 5, 'Salame', 5, 'Bife', 23]

print(f'{"-"*30}')
print(f'{"LISTA DE PREÇOS":^30}')
print(f'{"-"*30}')

for i in range(len(lista)):
    if i%2 == 0:
     print(f'{lista[i]:.<30}R${lista[(i+1)]:.2f}')