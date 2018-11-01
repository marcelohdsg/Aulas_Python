##Faça um algorítmo que leia um preço de um produto, e mostre seu novo preço, com 5% de desconto.

n = float(input('Qual o preço do produto? '))

print('O valor do produto com 5% de desconto é: {:.2f}'.format(n-(n*0.05)))
