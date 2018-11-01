colocados = 'São Paulo', 'Palmeiras', 'Internacional', 'Flamengo', 'Grêmio',\
            'Atlético', 'Cruzeiro', 'Corinthians', 'Fluminense', 'Atlético - PR', \
            'Samtos', 'Botafogo', 'Amériga - MG', 'Vitória', 'Bahia', 'Vasco', 'Chapecoense', \
            'Ceará', 'Sport', 'Paraná'

print(f'Lista de times: {colocados}')
print(f'Cinco primeiros times: {colocados[:5]}')
print(f'Quatro últimos times: {colocados[-5:]}')
print(f'Os times em ordem são: {times}')
print(f'O Chapecoense está na {colocados.index("Chapecoense")+1}º posição')


#print(f'CINCO PRIMEIROS COLOCADOS:')
#for cont in range(0, 5):
#    print(colocados[cont])

#print(f'\nQUATRO ÚLTIMOS COLOCADOS:')
#for cont1 in range(-4, 0):
#   print(colocados[cont1])

#print(sorted(colocados))

#for cont in range(len(colocados)):
#    if colocados[cont] == 'Chapecoense':
#        print(colocados[cont])
#        print(cont+1)

