def ler(n):
    lista = [0]*n
    for i in range(n):
        lista[i] = int(input(f'Digite o {i+1}º elemento da lista: '))
    return lista

def procura(elem, lis):
    cont = 0
    for i in range(n):
        if (lis[i] == elem):
            cont = cont + 1
    return cont


lis=[]
n = int(input('Quantos elementos tem o vetor? '))
lis = ler(n)
print(lis)
elem = int(input('Qual o elemento que deseja buscar? '))
quant = procura(elem, lis)
print(f'O valor {elem} apareceu {quant} vezes no vetor')
