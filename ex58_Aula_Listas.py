lista = list()
for cont in range(0, 5):
    lista.append(int(input('Entre com um valor: ')))

for c, v in enumerate(lista):
    if v == min(lista):
        print(f'O menor valor é {v}, na posição {c}')
    if v == max(lista):
        print(f'O maior valor é {v}, na posição {c}')




# lanche.append('Coockie') - Adicionar posição e adicionar elemento
# lanche.insert(0,'Coockie') - Adicionar elemento em qualquer outra posição
# del lanche[3] - Eliminar determinado indice
# lanche.pop(3) - Eliminar determinado indice
# lanche.pop(3) - Eliminar último indice
# lanche.remove('Suco') - Eliminar determinado elemento (Primeira ocorrência da lista)

# Listar valores da lista
# for v in lista:
#    print(f'{v}', end=' ')

# Listar valores E índices na lista
# for c, v in enumerate(lista):
#   print(f'Na posição {c}, valor: {v}')

# Incluir valores listas digitado
# lista = list()
# for cont in range(0, 5):
#    lista.append(int(input('Entre com um valor: ')))
