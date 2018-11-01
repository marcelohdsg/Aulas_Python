#Verifique se o nome da pessoa tem 'Silva'

n = str(input('Entre com seu nome completo: '))
n = n.title()

if ('Silva' in n) == True:
    print('\nSeu nome POSSUI "Silva"')

else:
    print('\nSeu nome NÃO possui "Silva"')