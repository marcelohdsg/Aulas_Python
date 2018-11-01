total = produto = barato = cont = 0
barateza = ''

while True:
    nome = input('\nNome: ')
    preco = float(input('Preço: R$'))
    cont += 1

    #contagem
    total += preco

    #quant. produto
    if preco > 1000:
        produto +=1

    #menor preço
    if cont == 1 or preco < barato:
        barato = preco
        barateza = nome

    #deseja continuar?
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').upper()

    #break
    if continuar == 'N':
        print(f'\nTotal de gastos: {total:.2f}')
        print(f'Produtos que custam mais de R$1000: {produto}')
        print(f'{barateza} é o produto mais barato e custa R${barato}')

        break
