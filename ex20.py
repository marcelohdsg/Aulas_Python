##O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
##Faça um programa que leia o nome dos quatro e mostre a ordem sorteada

from random import choice, shuffle

a1 = input('Entre com o nome do primeiro aluno: ')
a2 = input('Entre com o nome do segundo aluno: ')
a3 = input('Entre com o nome do terceiro aluno: ')
a4 = input('Entre com o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
s = shuffle(lista)

print('A ordem para apresentação é: {}' .format(lista))
