nome = input('Entre com seu nome completo: ')

div = nome.split()
print(
    '\nNome com letras minúsculas: {}'
    '\nNome com letras maiúsculas: {}'
    '\nO nome tem {} letras'
    '\nPrimeiro nome possui {} letras'
    .format(
        nome.lower(),
        nome.upper(),
        len(nome.replace(" ", "")),
        len(div[0])
    )
)


