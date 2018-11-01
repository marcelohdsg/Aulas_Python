lista = ['Jonas', 'Computador', 'Celular']

for p in lista: # para cada palavra da lista
    print(f'\nNa palavra {p} temos:', end=' ' ) #escreva a palavra

    for l in p: # para cada letra em palavra
        if l.lower() in 'aeiou': #coloque tudo em minusculo e verifique se está em aeiou
            print(f'{l}', end=' ') #se estiver, printe a letra
