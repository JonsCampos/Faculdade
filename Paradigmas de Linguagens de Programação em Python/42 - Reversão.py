lista = []
continua = 's'
while (continua.lower() == 's'):
    lista.append(int(input('Digite um valor para a lista: ')))
    continua = input('Deseja continuar? "s" para sim ou "n" para não: ')
lista.reverse()
print(lista)

'''
Reverse  método aplicado a lista que faz a lista ficar invertida
da ordem de alocação
'''

'''
Append  método aplicado na lista para alocar conteúdo na mesma
'''
