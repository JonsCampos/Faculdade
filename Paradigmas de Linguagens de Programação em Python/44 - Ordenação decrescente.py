lista = []
continua = 's'
while (continua.lower() == 's'):
    lista.append(int(input('Digite um valor para a lista: ')))
    continua = input('Deseja continuar? "s" para sim ou "n" para não: ')
lista.sort(reverse=True)
print(lista)

'''
Sort (reserve=True) método aplicado a lista, com parâmetro de reversão. 
que faz a ordenação decrescente
'''

'''
Append  método aplicado na lista para alocar conteúdo na mesma
'''
