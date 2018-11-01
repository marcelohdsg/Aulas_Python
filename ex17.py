##Um prof quer sortear um dos seus quatro alunos p apagar o quadro. Faça um programa que ajude ele, lendo o nome
##deles e escrevendo o nome do escolhido.

from random import choice

a1 = input('Entre com o nome do primeiro aluno: ')
a2 = input('Entre com o nome do segundo aluno: ')
a3 = input('Entre com o nome do terceiro aluno: ')
a4 = input('Entre com o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
e = choice(lista)

print('\nO aluno(a) sorteado(a) foi: {}'.format(e))

