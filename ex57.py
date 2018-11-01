#valores = []

#for cont in range(0, 3):
#    valores.append(input('Entre com um valor: '))

#for c, v in enumerate(valores): #comando 'enumerate' pega tanto o índice quanto o valor.
#    print(f' Em {c}, existe {v}')

valores = []

for cont in range(0, 5):
   valores.append(int(input(f'Entre com o valor na posição {cont}: '))) #appen = incluir na lista

for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}, {v}')

    if v == min(valores):
        print(f'{c}, {v}')



#for c, v in enumerate(valores): #comando 'enumerate' pega tanto o índice quanto o valor.
