string = lambda x: x
lista = list(map(str, string('Calin')))  # atribuição a um novo objeto
print(lista)

'''
Mesma coisa que:

string = ‘Calin'
lista = [] 
for i in string:
    lista.append(i) 
print(lista)
'''
