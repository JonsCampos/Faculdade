lista = []
continua = 's'
while (continua.lower() == 's'):
    lista.append(int(input('Digite um valor para a lista: ')))
    continua = input('Deseja continuar? "s" para sim ou "n" para não: ')
print(lista)
lista2 = sorted(lista)
print(lista2)

'''
Sempre que você quiser ordenar uma lista e colocar a
ordenação em cópia é necessário usar o sorted
'''
